import os
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI, OpenAIEmbeddings
from app.document_loader import load_documents


def get_rag_chain():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("환경 변수에서 OPENAI_API_KEY를 찾을 수 없습니다.")

    llm = OpenAI(
        model="gpt-4o-mini",
        openai_api_key=openai_api_key,
        temperature=0  # 답변의 일관성을 위해 온도를 0으로 설정
    )

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=openai_api_key
    )

    docs = load_documents("data/hr_policy_qa_samples.csv")
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={'k': 3}),
        chain_type="stuff",
        return_source_documents=True  # 답변의 근거 문서를 함께 반환할지 여부
    )
    return qa_chain