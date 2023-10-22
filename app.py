import os
import streamlit as st

from dotenv import load_dotenv

# Importing relevant packages
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from typing import Any

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

# Load data
documents = SimpleDirectoryReader("data").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Create query engine
query_engine = index.as_query_engine()

# Streamlit App
def run_streamlit() -> None:
    st.title("Streamlit Chatbot")
    st.write("Welcome to Streamlit chatbot. Type your query below.")

    user_input = st.text_input("Your question:")
    if user_input:
        response: Any = query_engine.query(user_input)
        st.write("Answer:", response)

if __name__ == "__main__":
    run_streamlit()
