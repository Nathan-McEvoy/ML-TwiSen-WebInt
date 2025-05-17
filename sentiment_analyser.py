import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
import joblib
import text_preprocessing

def clean_df_txt(dataframe):
    try:
        dataframe['text'] = text_preprocessing.clean_data(dataframe['text'])
    except Exception as e:
        print(f"Error cleaning text column {e}")
        dataframe['text'] = None

    dataframe.dropna(subset=['text'], inplace=True)
    return dataframe

cols = ['batch', 'game', 'class', 'text']
data = pd.read_csv("ml_data/twitter_training.csv", names=cols)
data.reset_index(drop=True, inplace=True)
test_data = pd.read_csv("ml_data/twitter_validation.csv", names=cols)
test_data.reset_index()

data = clean_df_txt(data)
test_data = clean_df_txt(test_data)

X = data['text']
y = data['class']
X_t = test_data['text']
y_t = test_data['class']

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=10000, ngram_range=(1, 2))),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(X, y)

y_pred = pipeline.predict(X_t)
print(classification_report(y_t, y_pred))

# joblib.dump(pipeline, 'ml_data/twitter_training.pkl')
print("Training Complete")