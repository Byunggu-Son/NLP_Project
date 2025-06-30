import gradio as gr
import requests

# FastAPI 서버의 URL
FASTAPI_URL = "http://127.0.0.1:8000/chat"

def chat_with_fastapi(question):
    try:
        response = requests.post(
            FASTAPI_URL,
            json={"question": question},
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()  # 오류가 있으면 예외 발생
        return response.json().get("answer", "답변을 받지 못했습니다.")
    except Exception as e:
        return f"오류 발생: {str(e)}"

# Gradio 인터페이스 정의
with gr.Blocks() as demo:
    gr.Markdown("# HR Q&A Chatbot")
    gr.Markdown("사내 HR 규정에 대한 질문을 입력하세요.")
    
    with gr.Row():
        question_input = gr.Textbox(label="질문", placeholder="질문을 입력하세요...")
        answer_output = gr.Textbox(label="답변", interactive=False)
    
    submit_button = gr.Button("질문 제출")
    submit_button.click(
        fn=chat_with_fastapi,
        inputs=question_input,
        outputs=answer_output
    )

# Gradio 앱 실행
demo.launch()