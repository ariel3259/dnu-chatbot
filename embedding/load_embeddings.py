from db.chroma_client import collection
import random

def load_embeddings(texts, embeddings):
    documents = [x.page_content for x in texts]
    ids = [f"{random.random()}" for x in texts]
    collection.add(
            embeddings=embeddings,
            documents=documents,
            ids=ids
    )
    print("Embedding loaded")