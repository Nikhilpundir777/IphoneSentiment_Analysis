import pandas as pd
import re
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_text(text):
    """
    Preprocesses the review text by converting to lowercase,
    removing non-alphabetic characters, and extra spaces.
    """
    text = text.lower()  
    text = re.sub(r"[^a-z\s]", "", text)  
    text = re.sub(r"\s+", " ", text).strip() 
    return text


def get_sentiment(text):
    """
    Analyzes the sentiment of a text and returns either 'positive' or 'negative'.
    """
    analysis = TextBlob(text)
    return "positive" if analysis.sentiment.polarity > 0 else "negative"


def extract_keywords(reviews_text, n=10):
    """
    Extracts top `n` keywords from the reviews using TF-IDF.
    """
    if not reviews_text.strip():  
        print("Warning: No content to extract keywords from.")
        return []

    vectorizer = TfidfVectorizer(stop_words="english", max_features=n)
    tfidf_matrix = vectorizer.fit_transform([reviews_text])
    keywords = vectorizer.get_feature_names_out()
    return keywords


def analyze_keywords(scraped_data):
    """
    Performs sentiment analysis on reviews and extracts top positive and negative keywords.
    """
    if not scraped_data:
        print("No reviews available for analysis.")
        return [], []

    # Convert scraped reviews to a DataFrame
    reviews_df = pd.DataFrame(scraped_data)

    # Ensure the content column exists and is not empty
    if "content" not in reviews_df or reviews_df["content"].dropna().empty:
        print("No valid content found in the reviews.")
        return [], []

    # Preprocess the review content
    reviews_df["content_clean"] = reviews_df["content"].dropna().apply(preprocess_text)

    # Perform sentiment analysis
    reviews_df["sentiment"] = reviews_df["content_clean"].apply(get_sentiment)

    # Separate positive and negative reviews
    positive_reviews = " ".join(reviews_df[reviews_df["sentiment"] == "positive"]["content_clean"])
    negative_reviews = " ".join(reviews_df[reviews_df["sentiment"] == "negative"]["content_clean"])

    # Extract keywords for positive and negative reviews
    best_keywords = extract_keywords(positive_reviews, n=10) if positive_reviews.strip() else []
    worst_keywords = extract_keywords(negative_reviews, n=10) if negative_reviews.strip() else []

    print("Best Keywords (Positive):", best_keywords)
    print("Worst Keywords (Negative):", worst_keywords)

    # Return the top keywords
    return best_keywords, worst_keywords
