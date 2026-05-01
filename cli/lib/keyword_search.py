import string

from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies, load_stopwords
from nltk.stem import PorterStemmer


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    stemmer = PorterStemmer()
    movies = load_movies()
    stopwords = load_stopwords()

    results = []
    for movie in movies:
        query_tokens = tokenize_text(query)
        clean_query_tokens = remove_stopwords(query_tokens, stopwords)
        title_tokens = tokenize_text(movie["title"])
        clean_title_tokens = remove_stopwords(title_tokens, stopwords)

        stemmered_query_tokens = [stemmer.stem(token) for token in clean_query_tokens]

        if has_matching_token(stemmered_query_tokens, clean_title_tokens):
            results.append(movie)
            if len(results) >= limit:
                break

    return results


def has_matching_token(query_tokens: list[str], title_tokens: list[str]) -> bool:
    for query_token in query_tokens:
        for title_token in title_tokens:
            if query_token in title_token:
                return True
    return False


def preprocess_text(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


def tokenize_text(text: str) -> list[str]:
    text = preprocess_text(text)
    tokens = text.split()
    valid_tokens = []
    for token in tokens:
        if token:
            valid_tokens.append(token)
    return valid_tokens

def remove_stopwords(tokens: list[str], stopwords: set[str]) -> list[str]:
    return [token for token in tokens if token not in stopwords]



