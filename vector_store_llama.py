import os
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

from llama_index import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
# query_engine.query("YOUR_QUESTION")
while True:
    query = input("Ask a question: ")
    if query == "exit":
        break
    else:
        print(query_engine.query(query))

x=0