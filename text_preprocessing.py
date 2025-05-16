import nltk
import string
import inflect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

def text_to_lowercase(text):
    return text.lower()

p = inflect.engine()
def convert_numbers(text):
    temp_str = text.split()
    new_str = []

    for word in temp_str:
        if word.isdigit():
            temp = p.number_to_words(word)
            new_str.append(temp)
        else:
            new_str.append(word)

    temp_str = ' '.join(new_str)
    return temp_str

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_excess_whitespace(text):
    return " ".join(text.split())

nltk.download('punkt_tab')
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return " ".join(filtered_text)

stemmer = PorterStemmer()
def stem_text(text):
    word_tokens = word_tokenize(text)
    stems = [stemmer.stem(word) for word in word_tokens]
    return " ".join(stems)

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
def lemma_words(text):
    word_tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(word) for word in word_tokens]
    return " ".join(lemmas)


def pipeline(*funcs):
    def inner(data):
        result = data
        for func in funcs:
            result = func(result)
        return result
    return inner

clean_data = pipeline(
    lambda x: text_to_lowercase(x),
    lambda x: convert_numbers(x),
    lambda x: remove_punctuation(x),
    lambda x: remove_excess_whitespace(x),
    lambda x: remove_stopwords(x),
    lambda x: stem_text(x),
    lambda x: lemma_words(x)
)