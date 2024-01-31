from chromadb import Client

chroma_db_client = Client()

collection = chroma_db_client.create_collection("dnu_70_2023_storage")
