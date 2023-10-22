import os
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
from typing import List, Any
# Import the function to get responses from your model
# from your_model import get_response

# Class to hold message data
class Message:
    def __init__(self, sender: str, content: str, timestamp: str):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp

# Function to display conversation
def display_conversation(conversation: List[Message]) -> None:
    for message in conversation:
        st.write(f"{message.timestamp} - {message.sender}: {message.content}")

# Load environment variables
load_dotenv()

# Get OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

# Placeholder for get_response function
def get_response(user_input: str) -> str:
    # Replace this with code to get a response from GPT-3 or another model
    return f"You said: {user_input}"

# Streamlit App
def run_streamlit() -> None:
    st.title("Streamlit ChatGPT-like Chatbot")
    st.write("Welcome to the ChatGPT-like chatbot. Type your query below.")

    # Load or initialize conversation
    conversation = st.session_state.get("conversation", [])

    user_input = st.text_input("Your question:")
    if user_input:
        # Save user message
        user_message = Message("You", user_input, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        conversation.append(user_message)

        # Get and save response
        response: str = get_response(user_input)
        bot_response = Message("Bot", response, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        conversation.append(bot_response)

        # Save conversation to state
        st.session_state["conversation"] = conversation

    # Display conversation
    display_conversation(conversation)

if __name__ == "__main__":
    run_streamlit()
