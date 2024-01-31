from embedding.split_texts import split_text
from embedding.make_embedding import make_embedding
from embedding.load_embeddings import load_embeddings
from db.chroma_client import collection
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
from embedding.mixtral_8x7b import Mixtral8x7B
import os

load_dotenv(find_dotenv(), override=True)
path = os.path.join(os.getcwd(), "embedding", "dnu_70_2023.txt")
texts = split_text(path)
if len(texts) != len(collection.get()["ids"]):
    embeddings = make_embedding(texts)
    load_embeddings(texts, embeddings)



class Question(BaseModel):
    content: str

app = FastAPI()

@app.post("/api/question")
def make_question(question: Question):
    mixtral = Mixtral8x7B()
    response = mixtral.make_answer(question.content)
    return response