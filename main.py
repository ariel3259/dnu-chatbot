from embedding.split_document import split_documents
from embedding.load_embeddings import load_embeddings
from db.chroma_client import collection
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
from embedding.mixtral_8x7b import Mixtral8x7B
import os

load_dotenv(find_dotenv(), override=True)
path = os.path.join(os.getcwd(), "embedding", "dataset_errepar.docx")
texts, metadatas = split_documents(path)
if len(texts) != len(collection.get()["ids"]):
    load_embeddings(texts, metadatas)



class Question(BaseModel):
    content: str

app = FastAPI()

@app.post("/api/question")
def make_question(question: Question):
    mixtral = Mixtral8x7B()
    response = mixtral.make_answer(question.content)
    return response