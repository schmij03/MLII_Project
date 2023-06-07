# language_detection.py

from langdetect import detect

def detect_language(df):
    for i in range(len(df)):
        try:
            df.loc[i, 'language'] = detect(df.loc[i, 'review_full'])
        except:
            df.loc[i, 'language'] = 'error'
            pass
    return df
