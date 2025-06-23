import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tkinter import Tk, Canvas, Entry, Button, Label, StringVar
from konlpy.tag import Okt
import pickle

# 경로 처리
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../models/sentiment_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "../models/vectorizer.pkl")

# 형태소 분석기 정의
okt = Okt()

def tokenize(text):
    return okt.morphs(text, stem=True)

# 모델과 벡터 불러오기
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

# 예측 함수
def analyze_sentiment():
    text = entry_1.get()
    tokenized = tokenize(text)
    transformed = vectorizer.transform([' '.join(tokenized)])
    prediction = model.predict(transformed)[0]

    if prediction == 1:
        result_var.set("긍정 리뷰입니다 :)")
        result_label.config(fg="green")
    else:
        result_var.set("부정 리뷰입니다 :(")
        result_label.config(fg="red")

# GUI 구성
window = Tk()
window.title("네이버 리뷰 감성 분석기")
window.geometry("520x300")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=300,
    width=520,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# 제목 텍스트
canvas.create_text(
    59.0,
    45.0,
    anchor="nw",
    text="네이버 리뷰 감성 분석기",
    fill="#000000",
    font=("Inter", 25, "bold")
)

# 입력창
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000000",
    highlightthickness=1
)
entry_1.place(
    x=100.0,
    y=100.0,
    width=320.0,
    height=30.0
)

# 결과 라벨
result_var = StringVar()
result_var.set("감정 분석 결과...")

result_label = Label(
    window,
    textvariable=result_var,
    bg="#FFFFFF",
    font=("Inter", 16),
    fg="#000000"
)
result_label.place(x=160, y=220)

# 버튼
button_1 = Button(
    text="분석하기",
    command=analyze_sentiment,
    bg="#000000",
    fg="white",
    font=("Inter", 12, "bold"),
    relief="flat"
)
button_1.place(
    x=220.0,
    y=150.0,
    width=80.0,
    height=35.0
)

window.resizable(False, False)
window.mainloop()
