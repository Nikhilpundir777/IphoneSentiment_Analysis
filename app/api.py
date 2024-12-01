from flask import Flask, request, jsonify
from textblob import TextBlob
from pymongo import MongoClient
from app.config import MONGO_URI, DB_NAME, COLLECTION_NAME
from app.database import connect_to_mongo

app = Flask(__name__)

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


@app.route('/api/sentiment', methods=['POST'])
def sentiment_analysis():
    """
    API to analyze sentiment for a given review.
    Expects JSON payload: {"review": "Your review text"}
    Returns: {"sentiment": "positive" / "negative" / "neutral"}
    """
    data = request.get_json()
    if not data or 'review' not in data:
        return jsonify({"error": "Invalid input. Provide a review text."}), 400

    review = data["review"]
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    sentiment = (
        "positive" if polarity > 0 else
        "negative" if polarity < 0 else
        "neutral"
    )
    return jsonify({"review": review, "sentiment": sentiment})


@app.route('/api/reviews', methods=['GET'])
def fetch_reviews():
    """
    API to fetch reviews based on filters: color, storage size, and rating.
    Query Parameters: ?color=Black&size=128GB&rating=5
    Returns: List of matching reviews.
    """
    color = request.args.get("color")
    size = request.args.get("size")
    rating = request.args.get("rating")

    query = {}
    if color:
        query["color"] = color
    if size:
        query["size"] = size
    if rating:
        try:
            query["rating"] = int(rating)
        except ValueError:
            return jsonify({"error": "Rating must be an integer."}), 400

    # Fetch reviews from MongoDB
    reviews = list(collection.find(query, {"_id": 0})) 

    if not reviews:
        return jsonify({"message": "No reviews found for the given filters."}), 404

    return jsonify({"reviews": reviews})


if __name__ == "__main__":
    app.run(debug=True)
