from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__, static_folder="static")
CORS(app)

# Replace with your Gemini API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def serve_index():
    return send_from_directory("static", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        prompt = data.get("message", "")
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "An error occurred while generating response."}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
