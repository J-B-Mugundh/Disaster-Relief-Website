import os
import torch
from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
from transformers import MobileBertForSequenceClassification, MobileBertTokenizer

# Initialize Flask
app = Flask(__name__)

# Load YOLOv8 Model (for Image Severity Detection)
yolo_model = YOLO("models/best_disaster_model.pt")

# Load MobileBERT Model (for Text Classification)
bert_model_path = "models/mobilebert"
bert_tokenizer = MobileBertTokenizer.from_pretrained(bert_model_path)
bert_model = MobileBertForSequenceClassification.from_pretrained(bert_model_path)

# Ensure uploads folder exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Homepage Route
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Processing Route
@app.route("/submit", methods=["POST"])
def process_request():
    result = {}

    # Process text input
    text_message = request.form.get("text_message", "")
    if text_message:
        inputs = bert_tokenizer(text_message, return_tensors="pt", padding=True, truncation=True)
        outputs = bert_model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()
        result["text_classification"] = "Disaster-related" if prediction == 1 else "Not disaster-related"

    # Process image input
    image_file = request.files.get("image_message")
    if image_file:
        image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(image_path)

        # Run YOLO model on image
        detections = yolo_model(image_path)

        # Extract the highest confidence label
        if detections and detections[0].boxes:
            highest_conf_box = max(detections[0].boxes, key=lambda b: b.conf)  # Get box with highest confidence
            highest_conf_label = detections[0].names[int(highest_conf_box.cls)]
            result["image_severity"] = [highest_conf_label]
        else:
            result["image_severity"] = ["No severe disaster detected"]

    return jsonify(result)

# Run the Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
