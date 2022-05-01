from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string


def filtered_sequence(input_sequence):
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))

    input_sequence = input_sequence.translate(str.maketrans('', '', string.punctuation))
    sequence_tokens = word_tokenize(input_sequence)
    filtered_sentence = [w for w in sequence_tokens if not w.lower() in stop_words]
    filtered_sentence = [ps.stem(w) for w in filtered_sentence]

    return filtered_sentence
