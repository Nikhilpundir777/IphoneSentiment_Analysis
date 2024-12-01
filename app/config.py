import os
from dotenv import load_dotenv

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# Load environment variables from .env file
load_dotenv()

# MongoDB URI from environment
MONGO_URI = os.getenv('MONGO_URI')

# Database and Collection names
DB_NAME = 'amazon_reviews'
COLLECTION_NAME = 'iphone_12_reviews'
