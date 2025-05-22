import pandas as pd
import joblib
import text_preprocessing

model = joblib.load('ml_data/twitter_training.pkl')

text_input = ''

input_series = pd.Series([text_input])
preprocessed_series = text_preprocessing.clean_data(input_series)

prediction = model.predict(preprocessed_series)
print(prediction)