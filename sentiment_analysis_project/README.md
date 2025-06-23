# 네이버 리뷰 감성 분석기

이 프로젝트는 네이버 영화 리뷰 데이터를 기반으로 한 감성 분석기입니다. 사용자는 GUI를 통해 리뷰를 입력하고, 해당 리뷰가 긍정적인지 부정적인지 확인할 수 있습니다.

## 📁 프로젝트 구조

```
sentiment_analysis_project/
├── app/
│   └── gradio_app.py
├── data/
│   ├── ratings_train.txt
│   └── ratings_test.txt
├── gui/
│   └── gui.py
├── models/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
├── train/
│   └── train_model.py
├── utils/   
│   └── preprocessing.py
├── requirements.txt
└── README.md
```

## 🛠 사용된 기술

- Python 3.9 이상
- scikit-learn
- pandas
- konlpy
- tkinter
- pickle
- Gradio

## 📦 설치 방법

1. 필요한 라이브러리 설치:
```bash
pip install -r requirements.txt
```

---

## 🤖 사용된 모델

### 1. 로지스틱 회귀 (Logistic Regression)
- **선택 이유**: 이진 분류에 최적화되어 있고 간단하면서도 안정적인 성능을 보임
- **장점**:
  - 확률 기반 예측으로 해석이 쉬움
  - 과적합에 강함
  - 학습 속도 빠름

### 2. 나이브 베이즈 (Naive Bayes) *(비교 모델)*
- **장점**:
  - 텍스트 기반 분류에 강력
  - 적은 학습 데이터에도 잘 동작
  - 매우 빠른 추론 속도

➡️ 테스트 결과, **로지스틱 회귀**가 더 우수한 성능을 보여 최종 모델로 채택되었습니다.

---

## 📚 이 프로젝트로 배운 점

- 형태소 기반 한국어 전처리의 중요성
- CountVectorizer를 활용한 텍스트 벡터화 방식 이해
- 다양한 모델 성능 평가 지표 (정확도, 정밀도, 재현율, F1-score)
- 예외 처리 및 하드코딩 제거를 통한 안정성 향상
- GUI 및 웹 UI 연동을 통한 사용자 친화적 배포 경험

---

## 🚀 실행 방법

### 1. 모델 학습 및 저장
```bash
python train/train_model.py
```

### 2. GUI 실행 (Tkinter)
```bash
python gui/gui.py
```

### 3. 웹 UI 실행 (Gradio)
```bash
cd app
python gradio_app.py
```
