import os
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from app.vector_store import get_vectorstore
from app.document_loader import load_documents

def get_rag_chain():
    """
    OpenAI GPT-4o-mini 모델을 사용한 RAG 체인 생성
    - 벡터스토어는 별도 모듈에서 관리
    - Returns: RetrievalQA 체인 객체
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 로드
    if not openai_api_key:
        raise ValueError("환경 변수에서 OPENAI_API_KEY를 찾을 수 없습니다.")  # 키 누락 시 에러 발생

    # LLM 모델 초기화
    llm = OpenAI(
        model="gpt-4o-mini",
        openai_api_key=openai_api_key, # API 키 전달
        temperature=0  # 답변 일관성 위해 온도 0 설정
    )

    # 문서 로드
    docs = load_documents("data/hr_policy_qa_samples.csv")  # 데이터 로더 호출

    # 벡터스토어 생성 (별도 모듈에서 처리)
    vectorstore = get_vectorstore(docs)  # vector_store.py 호출

    # RAG 체인 조립
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={'k': 3}),  # 상위 3개 문서 검색
        chain_type="stuff",  # 검색 문서 한꺼번에 처리
        return_source_documents=False  # 근거 문서 반환 여부
    )

    return qa_chain