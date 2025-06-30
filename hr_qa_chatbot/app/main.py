from dotenv import load_dotenv
load_dotenv()  # .env 파일에서 api key로드

from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chain import get_rag_chain

app = FastAPI(
    title="HR Q&A Chatbot API",
    description="OpenAI GPT와 RAG를 이용한 사내 HR 규정 Q&A 챗봇"
)

# 서버 시작 시 RAG 체인을 미리 생성
rag_chain = get_rag_chain()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat", summary="챗봇에게 질문하기")
async def chat(request: ChatRequest):
    question = request.question

    if not question:
        return {"error": "질문 내용이 없습니다."}

    result = await rag_chain.ainvoke({"query": question})
    return {"answer": result.get("result")}