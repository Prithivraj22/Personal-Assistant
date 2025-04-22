from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from utils.speech_to_text import transcribe_audio

app = Flask(__name__)
CORS(app)

model = pickle.load(open("D:\Prithiv\Flask learning\voice_assistant\voice_assistant_project\backend\model\logistic_model.pkl", "rb"))

@app.route('/')
def index():
    return 'Flask backend is working!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get("message", "")
    prediction = model.predict([[len(text), text.count(" "), text.count("a")]])
    return jsonify({"response": f"Model Prediction: {prediction[0]}"})

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    text = transcribe_audio(file)
    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(debug=True)
