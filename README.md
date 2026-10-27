# Recommendor 🎬

**Your taste. Your next obsession.**

Recommendor is a content-based movie recommendation system that suggests movies based on genres, keywords, and story descriptions. It uses Python, Pandas, Scikit-learn, TF-IDF vectorization, and cosine similarity to help users discover movies they may enjoy.
## ✨ Features

- 🎥 Interactive Streamlit web interface
- 🔍 Search and select movies from the dataset
- 🧠 Content-based movie recommendations
- 📊 TF-IDF vectorization for movie text features
- 🎯 Cosine similarity to identify similar movies
- 🎨 Netflix-inspired dark theme with red accents
- ✨ Animated UI elements and movie cards

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- HTML and CSS

## 📁 Project Structure

```text
movie-recommendation-system/
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── tmdb_5000_movies.csv
└── notebooks/
    └── original_notebook.ipynb
```

*Your notebook filename may be different.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd movie-recommendation-system
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Prepare the dataset

Place `tmdb_5000_movies.csv` inside the `data/` directory.

The expected file path is:

```text
data/tmdb_5000_movies.csv
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 🧠 How It Works

1. Loads movie information from the CSV dataset.
2. Extracts movie genres, keywords, and overviews.
3. Combines these text features into movie tags.
4. Converts the tags into numerical features using TF-IDF.
5. Calculates cosine similarity between movies.
6. Returns the most similar movies for the selected title.

## 🖼️ Images

The interface uses externally hosted cinematic images for its visual presentation. An internet connection is required to load these images.

## 📂 Dataset

The application expects the TMDB 5000 movies CSV file in the `data/` directory. Include the dataset in the repository only if its source terms permit redistribution; otherwise, provide instructions for obtaining it separately.

## 🚀 Future Improvements

- Movie ratings and release years
- Movie details and descriptions
- Watchlist and favorites
- More personalized recommendations
- Deployment as a public web application

## 👨‍💻 Author

**Abdul Rehman**

AI & Machine Learning | Python | Data Science

---

*Built as a machine learning and web development portfolio project.*
