import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Function to simulate text-to-speech (replace with actual TTS library)
def text_to_speech(text):
    print(f"[TTS] {text}")  # Simulating speech output

# Optimized Model Configuration for Speed
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
    system_instruction="Personality & Tone: Gen Z Bestie Vibes...",
)

# Start Chat Session with history tracking
chat_session = model.start_chat(history=[])

print("Bot: Hello, how can I help you?")
text_to_speech("Hello, how can I help you?")

while True:
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Bye! Take care. 😊")
        break

    # Send message and maintain history
    response = chat_session.send_message(user_input, history=chat_session.history)
    model_response = response.text

    print(f'Bot: {model_response}')
    text_to_speech(model_response)
