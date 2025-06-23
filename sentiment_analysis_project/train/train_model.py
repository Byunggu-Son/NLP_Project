import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from utils.preprocessing import load_data, tokenize, preprocess_data

# 데이터 로드 및 전처리
data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
train_df = preprocess_data(load_data(os.path.join(data_dir, "ratings_train.txt")))
test_df = preprocess_data(load_data(os.path.join(data_dir, "ratings_test.txt")))

# 벡터화
vectorizer = CountVectorizer(tokenizer=tokenize)
X_train = vectorizer.fit_transform(train_df['document'])
y_train = train_df['label']

X_test = vectorizer.transform(test_df['document'])
y_test = test_df['label']

# 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 성능 출력
accuracy = accuracy_score(y_test, model.predict(X_test))
print("정확도:", accuracy)

# 저장
models_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "models")
os.makedirs(models_dir, exist_ok=True)

with open(os.path.join(models_dir, "sentiment_model.pkl"), "wb") as f:
    pickle.dump(model, f)
with open(os.path.join(models_dir, "vectorizer.pkl"), "wb") as f:
    pickle.dump(vectorizer, f)
