import pandas as pd
from langchain_core.documents import Document

def load_documents(path: str):
    df = pd.read_csv(path)
    
    # itertuples()를 사용하여 더 빠르고 효율적으로 반복!
    document_list = []
    for row in df.itertuples(index=False):
        doc = Document(
            page_content=row.Answer,
            metadata={"question": row.Question}
        )
        document_list.append(doc)
        
    return document_list
