from db.chroma_client import collection
import uuid

def load_embeddings(texts, metadatas):
    ids = [str(uuid.uuid4()) for _ in texts]
    collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids
    )
    print("Embedding loaded")