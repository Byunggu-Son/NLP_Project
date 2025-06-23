# 네이버 리뷰 감성 분석기

이 프로젝트는 네이버 영화 리뷰 데이터를 기반으로 한 감성 분석기입니다. 사용자는 GUI를 통해 리뷰를 입력하고, 해당 리뷰가 긍정적인지 부정적인지 확인할 수 있습니다.

## 📁 프로젝트 구조

sentiment_analysis_project/
├── data/
│ ├── ratings_train.txt
│ └── ratings_test.txt
├── models/
│ ├── sentiment_model.pkl
│ └── vectorizer.pkl
├── gui/
│ └── gui.py
├── preprocessing/
│ └── preprocessing.py
├── train/
│ └── train_model.py
├── requirements.txt
└── README.md

## 🛠 사용된 기술

- Python 3.9 이상
- scikit-learn
- pandas
- konlpy
- tkinter
- pickle

## 📦 설치 방법

1. 필요한 라이브러리 설치:

pip install -r requirements.txt

## 프로젝트 내용

- 자연어 전처리 및 형태소 분석
- CountVectorizer를 통한 텍스트 벡터화
- 머신러닝 모델 학습, 평가 및 저장
- GUI를 통한 사용자 인터페이스 구현
- 코드 구조화 및 예외 처리


