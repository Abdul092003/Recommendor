
import ast
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------------------
# 1. Load movie dataset
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "tmdb_5000_movies.csv"

dataset = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Original dataset shape:", dataset.shape)


# --------------------------------------------------
# 2. Select required columns
# --------------------------------------------------

movies = dataset[["title", "genres", "keywords", "overview"]].copy()

# Missing overview ko empty string se replace karo
movies["overview"] = movies["overview"].fillna("")

# Rows ko 0 se dobara number do, taake similarity matrix
# aur movies ki row positions ek doosre se match karein.
movies = movies.dropna(subset=["title", "genres", "keywords"])
movies = movies.reset_index(drop=True)


# --------------------------------------------------
# 3. Extract genre and keyword names
# --------------------------------------------------

def get_names(text):
    """Extract names from a TMDB genre/keyword value."""

    if isinstance(text, list):
        data = text
    else:
        data = ast.literal_eval(text)

    return [
        item["name"]
        for item in data
        if isinstance(item, dict) and "name" in item
    ]


movies["genres"] = movies["genres"].apply(get_names)
movies["keywords"] = movies["keywords"].apply(get_names)


# --------------------------------------------------
# 4. Combine movie information into tags
# --------------------------------------------------

movies["tags"] = (
    movies["genres"].apply(lambda items: " ".join(items))
    + " "
    + movies["keywords"].apply(lambda items: " ".join(items))
    + " "
    + movies["overview"]
)

# Remove unnecessary spaces
movies["tags"] = movies["tags"].str.strip()


# --------------------------------------------------
# 5. Convert text into numerical features using TF-IDF
# --------------------------------------------------

tfidf = TfidfVectorizer(stop_words="english")

matrix = tfidf.fit_transform(movies["tags"])

print("TF-IDF matrix shape:", matrix.shape)


# --------------------------------------------------
# 6. Calculate movie similarity
# --------------------------------------------------

similarity = cosine_similarity(matrix)

print("Similarity matrix shape:", similarity.shape)


# --------------------------------------------------
# 7. Recommend similar movies
# --------------------------------------------------

def recommend(movie_name, limit=10):
    """Return movies most similar to the selected movie."""

    matches = movies.index[
        movies["title"].str.casefold() == movie_name.strip().casefold()
    ]

    if len(matches) == 0:
        return ["Movie dataset mein nahi mili. Title check karo."]

    index = matches[0]

    scores = list(enumerate(similarity[index]))

    # Selected movie ko khud recommendations se exclude karo
    scores = [
        (row, score)
        for row, score in scores
        if row != index
    ]

    scores = sorted(
        scores,
        key=lambda item: item[1],
        reverse=True
    )

    top_movies = scores[:limit]

    recommendations = []

    for row, score in top_movies:
        recommendations.append(movies.iloc[row]["title"])

    return recommendations


# --------------------------------------------------
# 8. Test the recommendation system
# --------------------------------------------------

if __name__ == "__main__":
    movie_name = "Harry Potter and the Half-Blood Prince"

    print(f"\nRecommendations for: {movie_name}")

    results = recommend(movie_name)

    for number, title in enumerate(results, start=1):
        print(f"{number}. {title}")
