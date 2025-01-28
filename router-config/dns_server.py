from dnslib import DNSRecord, QTYPE, RR, A
from socketserver import UDPServer, BaseRequestHandler

HOST = "0.0.0.0"
PORT = 53
REDIRECT_IP = "192.168.0.25"  # Your laptop's static IP

class DNSHandler(BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        dns_record = DNSRecord.parse(data)
        reply = dns_record.reply()
        for question in dns_record.questions:
            qname = str(question.qname)
            qtype = QTYPE[question.qtype]
            print(f"DNS Query: {qname} Type: {qtype}")
            # Redirect all queries to the REDIRECT_IP
            reply.add_answer(RR(qname, QTYPE.A, rdata=A(REDIRECT_IP), ttl=60))
        socket.sendto(reply.pack(), self.client_address)

if __name__ == "__main__":
    with UDPServer((HOST, PORT), DNSHandler) as server:
        print(f"DNS server running on {HOST}:{PORT}, redirecting to {REDIRECT_IP}")
        server.serve_forever()
