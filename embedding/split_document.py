from docx import Document
import re
import os 
title_pattern = re.compile(r'título [ivxlcdm]+')
chapter_pattern = re.compile(r'capítulo [ivxlcdm]+')
article_pattern = re.compile(r'art. [0-9]{1,} -')

def split_documents():

    path = os.path.join(os.getcwd(), "embedding", "dataset_errepar.docx")
    with open(path, 'rb') as f:
        document = Document(f)
        f.close()
    paragraphs = document.paragraphs
    title = ""
    chapter = ""
    article = ""
    chunks: list[str] = []
    chunk = ""
    for paragraph in paragraphs:
        text = paragraph.text.lower()
        title_match = title_pattern.match(text)
        chapter_match = chapter_pattern.match(text)
        article_match = article_pattern.match(text)
    
        if title_match is None and chapter_match is None and article_match is None and chunk != "":
            try:
                chunk_index = chunks.index(chunk)
                chunk += text
                chunks[chunk_index] = chunk
            except Exception:
                pass
        if title_match is not None or chapter_match is not None:
            chunks.append(article)
            article = ""
            if title_match is not None:
                title = title_match.string
                chapter = ""
            if chapter_match is not None:
                chapter = chapter_match.string
        if title != "" and chapter != "" and article_match is not None:
            chunk = f"{title} - {chapter} {text}"
            chunks.append(chunk)
        if chapter == "" and title != "" and article_match is not None:
            if article == "":
                article = f" {title} - {text}"
            elif article != "":
                article += f" {text}"
            
            
        
            
    print(chunks[3])
      

        

split_documents()