import pandas as pd
from konlpy.tag import Okt

okt = Okt()

def tokenize(text):
    return okt.morphs(text, stem=True)

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, sep='\t', encoding='utf-8').dropna()
        return df
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        exit()

def preprocess_data(df):
    df['document'] = df['document'].str.strip()
    df['document'] = df['document'].fillna("")
    return df
