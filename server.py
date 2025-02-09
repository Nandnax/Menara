from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Function to simulate text-to-speech (replace with actual TTS library)
def text_to_speech(text):
    print(f"[TTS] {text}")  # Simulating speech output

# Model Configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 500,
}

# Initialize Generative Model
model = genai.GenerativeModel(
    model_name="gemini-2.0-pro-exp-02-05",
    generation_config=generation_config,
    system_instruction="Gen Z Bestie Vibes: Casual, friendly, and relatable...",
)

# Start Chat Session with history tracking
chat_session = model.start_chat(history=[])

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    response = chat_session.send_message(user_message, history=chat_session.history)
    model_response = response.text

    return jsonify({"reply": model_response})

if __name__ == "__main__":
    print("Bot: Hello, how can I help you?")
    text_to_speech("Hello, how can I help you?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Bye! Take care. 😊")
            break
        
        response = chat_session.send_message(user_input, history=chat_session.history)
        model_response = response.text
        
        print(f'Bot: {model_response}')
        text_to_speech(model_response)
    
    app.run(debug=True, port=5000)
