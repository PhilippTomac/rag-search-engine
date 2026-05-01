import json
import os

DEFAULT_SEARCH_LIMIT = 10

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "movies.json")


def load_movies() -> list[dict]:
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return data["movies"]

def load_stopwords() -> set[str]:
    stopwords_path = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")
    with open(stopwords_path, "r") as f:
        stopwords = set(line.strip() for line in f)
    return stopwords
