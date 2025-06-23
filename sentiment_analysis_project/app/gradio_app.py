import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import gradio as gr
import joblib
from konlpy.tag import Okt

# 형태소 분석기 정의
okt = Okt()

def tokenize(text):
    return okt.morphs(text, stem=True)

# 모델 및 벡터 불러오기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../models/sentiment_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "../models/vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# 예측 함수
def predict_sentiment(text):
    if not text.strip():
        return "입력값이 없습니다."
    tokens = tokenize(text)
    transformed = vectorizer.transform([' '.join(tokens)])
    prediction = model.predict(transformed)[0]
    return "긍정적인 문장입니다!" if prediction == 1 else "부정적인 문장입니다."

# Gradio 인터페이스 생성
iface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="리뷰를 입력하세요!", label="리뷰 입력"),
    outputs=gr.Text(label="감성 분석 결과"),
    title="네이버 영화 리뷰 감성 분석기 (NSMC)",
    description="머신러닝 기반 Logistic Regression 감성 분석 프로젝트"
)

if __name__ == "__main__":
    iface.launch()
