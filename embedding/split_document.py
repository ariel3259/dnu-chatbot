from docx import Document
import re
import os 
title_pattern = re.compile(r'título [ivxlcdm]+')
chapter_pattern = re.compile(r'capítulo [ivxlcdm]+')


def split_documents():

    path = os.path.join(os.getcwd(), "embedding", "dataset_errepar.docx")
    with open(path, 'rb') as f:
        document = Document(f)
        f.close()
    paragraphs = document.paragraphs
    title = ""
    chapter = ""
    article = ""
    chunks = []
    for paragraph in paragraphs:
        text = paragraph.text.lower()
        chunk = ""
        if title_pattern.match(text) is not None:
            title_match = title_pattern.match(text)
            title = title_match.string
            
        if chapter_pattern.match(text) is None:
            article = text
            chunk = title + article
            chunks.append(chunk)
        else:
                chapter_match = chapter_pattern.match(text)
                chatpter = chapter_match.string
                chunk += chatpter
                chunk += " " + text.replace(title, "").replace(chapter, "")
        print(chunk)
      
      

        

split_documents()