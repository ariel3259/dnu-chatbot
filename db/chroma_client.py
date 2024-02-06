from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import os

embed_fn = SentenceTransformerEmbeddingFunction(model_name="multi-qa-MiniLM-L6-cos-v1")
path = os.path.join(os.getcwd(), "db")
chroma_db_client = PersistentClient(path)

try:
    collection = chroma_db_client.get_collection("dnu_70_2023_storage", embedding_function=embed_fn)
except ValueError:
    collection = chroma_db_client.create_collection("dnu_70_2023_storage", embedding_function=embed_fn)
