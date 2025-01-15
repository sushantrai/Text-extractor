from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from extractor import extract_text_auto

app = Flask(__name__)
CORS(app)

# Define upload folder
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Use the extractor to process the file and extract text
    extracted_text = extract_text_auto(file_path)

    os.remove(file_path)

    if extracted_text:
        return jsonify({"text": extracted_text}), 200
    else:
        return jsonify({"error": "Failed to extract text"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
