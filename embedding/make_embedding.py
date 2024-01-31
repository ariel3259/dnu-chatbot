from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_core.documents import Document

def make_embedding(texts: list[Document]):
    embedding_function = SentenceTransformerEmbeddings(model_name="multi-qa-MiniLM-L6-cos-v1")
    embeddings = [embedding_function.embed_query(x.page_content) for x in texts]
    return embeddings