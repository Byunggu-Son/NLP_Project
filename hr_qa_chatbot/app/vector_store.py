import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def get_vectorstore(docs):
    openai_api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 로드
    if not openai_api_key:
        raise ValueError("환경 변수에서 OPENAI_API_KEY를 찾을 수 없습니다.")  # 키 누락 시 에러

    # 임베딩 모델 초기화
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",  # 임베딩 모델 지정
        openai_api_key=openai_api_key  # API 키 전달
    )

    # 문서 벡터화 및 저장소 생성
    vectorstore = Chroma.from_documents(
        documents=docs,  # 입력 문서
        embedding=embeddings  # 임베딩 모델 사용
    )

    return vectorstore  # 벡터스토어 반환