from app.scraper import get_all_reviews
from app.database import connect_to_mongo, save_reviews_to_mongo
from app.keyword_analysis import analyze_keywords
from app.api import app  
from app.config import MONGO_URI, DB_NAME, COLLECTION_NAME


def main():
    # Base URL for reviews
    base_review_url = " https://www.amazon.in/Apple-New-iPhone-12-128GB/dp/B08L5TNJHG/"

    # Step 1: Scrape Amazon reviews
    reviews = get_all_reviews(base_review_url, max_pages=5)
    print(f"Scraped {len(reviews)} reviews.")

    # Step 2: Save reviews to MongoDB
    collection = connect_to_mongo(MONGO_URI, DB_NAME, COLLECTION_NAME)
    save_reviews_to_mongo(collection, reviews)

     # Step 3: Analyze keywords
    best_keywords, worst_keywords = analyze_keywords(reviews)
    print(f"Top Keywords: {best_keywords}")
    print(f"Least Keywords: {worst_keywords}")

   

if __name__ == "__main__":
    
    main()

    app.run(debug=True)