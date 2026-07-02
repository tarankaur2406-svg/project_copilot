import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

def get_ai_response(user_message, chat_history=None):

    if chat_history is None:
        chat_history = []

    try:
        conversation = ""

        for msg in chat_history:
            role = "User" if msg["role"] == "user" else "Assistant"
            conversation += f"{role}: {msg['content']}\n"

        conversation += f"User: {user_message}\nAssistant:"

        response = model.generate_content(conversation)

        return response.text

    except Exception as e:
        return f"Error: {e}"