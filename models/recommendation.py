from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_books(books, book_id, top_n=5):

    tfidf = TfidfVectorizer(stop_words="english")

    matrix = tfidf.fit_transform(books["description"].fillna(""))

    cosine_sim = cosine_similarity(matrix)

    idx = books[books["id"] == book_id].index[0]

    scores = list(enumerate(cosine_sim[idx]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    book_indices = [i[0] for i in scores[1:top_n+1]]

    return books.iloc[book_indices]