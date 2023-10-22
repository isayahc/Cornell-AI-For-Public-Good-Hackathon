import streamlit as st
from datetime import datetime
from typing import List, Dict

class Message:
    def __init__(self, sender: str, content: str, timestamp: str):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp

def display_conversation(conversation: List[Message]) -> None:
    for message in conversation:
        st.write(f"{message.timestamp} - {message.sender}: {message.content}")

def main():
    st.title("Conversational Chain with Streamlit")
    
    # Load conversation from state or start a new conversation
    conversation = st.session_state.get("conversation", [])
    
    user_input = st.text_input("You:")
    if user_input:
        user_message = Message("You", user_input, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        conversation.append(user_message)
        
        # Here you could add code to generate a response and append it to the conversation
        # For simplicity, we'll just echo the user input
        bot_response = Message("Bot", f"You said: {user_input}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        conversation.append(bot_response)
        
        # Save conversation to state
        st.session_state["conversation"] = conversation
    
    if st.button("Display Conversation"):
        display_conversation(conversation)
    
if __name__ == "__main__":
    main()
