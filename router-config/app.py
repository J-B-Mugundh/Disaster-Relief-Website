from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def captive_portal():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Disaster Relief Support</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #fff;
        }
        .container {
            background: #ffffff;
            color: #333;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
            text-align: center;
            width: 90%;
            max-width: 720px;
        }
        h1 {
            margin-bottom: 20px;
            font-size: 2rem;
            color: #6a11cb;
        }
        p {
            font-size: 1rem;
            margin-bottom: 20px;
            line-height: 1.5;
        }
        textarea, input[type=\"file\"] {
            margin: 10px 0;
            width: 80%;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 1rem;
        }
        button {
            margin-top: 20px;
            padding: 15px;
            width: 100%;
            background: #6a11cb;
            color: #fff;
            font-size: 1.2rem;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        button:hover {
            background: #2575fc;
        }
        footer {
            margin-top: 20px;
            font-size: 0.9rem;
            color: #aaa;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>NGN Labs Disaster Relief Support</h1>
        <img src="https://ngnlab.org/assets/img/logo_2.jpg" alt="NGN Labs Logo" style="width: 100%; height: auto; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);">
        <p>We are here to help. Share your message or upload an image to let us know how we can assist you.</p>
        <form action="/submit" method="POST" enctype="multipart/form-data">
            <textarea name="text_message" placeholder="Type your message here..." rows="4"></textarea>
            <input type="file" name="image_message" accept="image/*">
            <button type="submit">Submit</button>
        </form>
        <footer>&copy; 2025 NGN Labs Disaster Relief Support. All Rights Reserved.</footer>
    </div>
</body>
</html>

    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
