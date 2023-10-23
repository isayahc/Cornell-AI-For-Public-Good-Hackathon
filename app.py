from typing import Dict, List
import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

# Function to load data
@st.cache_resource(show_spinner=False)
def load_data() -> VectorStoreIndex:
    with st.spinner(text="Loading and indexing the Streamlit docs – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt=chat_prompt))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

# Header and chat prompt
st.header("🗽 NYC Skill Accelerator 💬 📚")
st.subheader("Hello NYer, looking for a way to learn new interesting skills! Well Ask me and I can help you. Don't speak English? No worries.")
chat_prompt = """
You are given a .csv file for program related to career training. 
You must provide the user with answers pertaining to career training and courses that are avaiable based on the user's questions. 
Please only rely on the csv.

make sure to provide
course name | Location | Duration | Cost | Prerequisites | Description\n

Please say yes sir or yes madam
"""

# API Key input
openai.api_key = st.text_input("Enter your OPEN_API_KEY:", type="password")

# Initialize the chat message history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me questions about classes in your borough!"}
    ]

# Load data and initialize the chat engine
index = load_data()
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

# Handle user input
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display the chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Generate a response if the last message is not from the assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)
