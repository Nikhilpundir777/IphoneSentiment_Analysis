from pymongo import MongoClient

def connect_to_mongo(uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def save_reviews_to_mongo(collection, reviews):
    collection.insert_many(reviews)
    print(f"Saved {len(reviews)} reviews to MongoDB.")