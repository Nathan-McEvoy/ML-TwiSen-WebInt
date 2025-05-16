import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import math

cols = ['batch', 'game', 'class', 'text']
data = pd.read_csv("ml_data/twitter_training.csv", names=cols)
data.reset_index()

# scrub nan values from dataset
for index, row in data.iterrows():
    if isinstance(row['text'], str):
        continue
    if math.isnan(row['text']):
        data.drop(index, inplace=True)

X = data['text']
y = data['class']


pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english')),
    ('clf', LogisticRegression(multi_class='multinomial', max_iter=1000))
])

pipeline.fit(X, y)

joblib.dump(pipeline, 'ml_data/twitter_training.pkl')
print("Training Complete")