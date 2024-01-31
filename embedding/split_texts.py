from langchain.text_splitter import RecursiveCharacterTextSplitter as RC
from langchain_core.documents import Document

def split_text(path: str):
    with open(path, encoding="utf-8") as f:
        print(f.readable())
        if f.readable() is False:
            raise Exception("El archivo no puede ser leido")
        text = f.read()
        f.close()
    text_splitter = RC(
        chunk_size=200,
        chunk_overlap=20,
        length_function=len
    )
    texts: list[Document]= text_splitter.create_documents([text])
    return texts
    