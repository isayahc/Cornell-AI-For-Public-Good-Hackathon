# Import Chroma and instantiate a client. The default Chroma client is ephemeral, meaning it will not save to disk.
import chromadb

client = chromadb.Client()

import chromadb

client = chromadb.Client()

collection = client.get_collection("new_york_data")

x=0
