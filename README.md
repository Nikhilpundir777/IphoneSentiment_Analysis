iPhone 12 Review Scraper and Sentiment Analysis
This project involves scraping reviews for the iPhone 12 from Amazon, performing sentiment analysis on the scraped data, and exposing APIs to analyze and retrieve reviews based on filters.

Features
Web Scraping:

1.Scrape multiple pages of reviews for the iPhone 12.
Extract review details:
Review Title
Review Text
Style Name (Storage size)
Color
Verified Purchase
Save the scraped data into a MongoDB database.

2.Keyword Analysis:
Identify the best keywords (positive reviews) and worst keywords (negative reviews)

3.Sentiment Analysis:
Perform sentiment analysis on the scraped reviews.
Use the TextBlob library for polarity scoring.

4.REST APIs:
Sentiment Analysis API: Analyze the sentiment of a given review text.
Review Retrieval API: Retrieve reviews filtered by:
Color
Storage size
Rating
