from docx import Document
import re

title_pattern = re.compile(r'título (?=[mdclxvi)m*(c[md]|d?c{0,3})(x[cl]|l?x{0,3})(i[xv]|v?i{0,3})+ - ')
chapter_pattern = re.compile(r'capítulo (?=[mdclxvi)m*(c[md]|d?c{0,3})(x[cl]|l?x{0,3})(i[xv]|v?i{0,3})+ - ')
article_pattern = re.compile(r'art. [0-9]{1,} -')

def split_documents(path):

    with open(path, 'rb') as f:
        document = Document(f)
        f.close()
    paragraphs = document.paragraphs
    title = ""
    chapter = ""
    article = ""
    chunks: list[str] = []
    chunk = ""
    metadatas: list[str] = []
    metadata = {
        "title": "",
        "chapter": "-",
    }
    for paragraph in paragraphs:
        text = paragraph.text.lower()
        title_match = title_pattern.match(text)
        chapter_match = chapter_pattern.match(text)
        article_match = article_pattern.match(text)
        ##add more paragraph to chunks if there're more than one
        if title_match is None and chapter_match is None and article_match is None and chunk != "":
            try:
                chunk_index = chunks.index(chunk)
                chunk += text
                chunks[chunk_index] = chunk
            except Exception:
                pass
        if title_match is None and chapter_match is None and article_match is None and article != "":
            try:
                article += text
            except Exception:
                pass
        
        if title_match is not None or chapter_match is not None:
            if article != "":
                chunks.append(article.lower())
                article = ""
            
            if title_match is not None:
                title = title_match.string  
                metadata["title"] = re.sub(title_pattern, "", title)
                metadata["chapter"] = "-"
                chapter = ""
            if chapter_match is not None:
                chapter = chapter_match.string
                metadata["chapter"] = re.sub(chapter_pattern, "", chapter)

        if title != "" and chapter != "" and article_match is not None:
            chunk = f"{title} - {chapter} {text}"
            if chunk != "":
                chunks.append(chunk)
                metadatas.append(metadata)
        if chapter == "" and title != "" and article_match is not None:
            if article == "":
                article = f" {title} - {text}"
                metadatas.append(metadata)
            elif article != "":
                article += f" {text}"
    # Add the last title
    article = article.replace("texto s/decreto 70/2023 - bo: 21/12/2023fuente: d. 70/2023aplicación: a partir del 30/12/2023- micrositio: reformas y medidas del gobierno", "")
    if (article != ""):
        chunks.append(article)    

    return (chunks, metadatas)