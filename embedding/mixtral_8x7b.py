from db.chroma_client import collection
import os
import requests

class Mixtral8x7B:

    def __init__(self):
        token = os.environ.get("HF_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {token}"
        }
        self.primer = "Sos un un experto en leyes y politica. Responde las preguntas del usuario, usa la información provista para informar tu respuesta. En caso de no tener informacion suficiente, recomenda visitar errepar.com."
        
    def make_answer(self, question):
        query_result =collection.query(
            query_texts=[question],
            n_results = 5
        )
        payload = {
            "inputs": f"""{self.primer}
            Informacion: {query_result["documents"]}
            Pregunta del usuario: {question}
            Respuesta:""",
            "parameters": {
                "max_new_tokens": 4000
            }
        }
        response = requests.post(
            "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
            headers = self.headers,
            json = payload
        )
        json = response.json()
        answer = json[0]["generated_text"].split("\n")[3].split(": ")[1]
        return { "answer": answer }
        
        

