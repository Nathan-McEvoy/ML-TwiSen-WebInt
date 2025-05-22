import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess_text_series(series):
    """Vectorised preprocessing for a pandas Series."""
    series = series.str.lower()

    translator = str.maketrans('', '', string.punctuation)
    series = series.str.translate(translator)

    series = series.str.strip().str.replace(r'\s+', ' ', regex=True)

    return series

def tokenise_and_process(text):
    """Tokenise and apply stopword removal, stemming and lemmatization in one pass."""
    tokens = word_tokenize(text)
    processed = [lemmatizer.lemmatize(stemmer.stem(word)) for word in tokens if word not in stop_words]
    return ' '.join(processed)

def clean_data(series):
    """Main cleaning function for a pandas Series."""
    series = preprocess_text_series(series)
    series = series.apply(lambda x: tokenise_and_process(x) if isinstance(x, str) and x else '')
    return series