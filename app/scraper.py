import requests
from bs4 import BeautifulSoup
import time

custom_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

def get_reviews_from_page(url):
    """
    Scrapes reviews from a single Amazon review page.
    """
    response = requests.get(url, headers=custom_headers)
    if response.status_code != 200:
        print(f"Failed to fetch page: {url}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    review_elements = soup.select("div[data-hook='review']")

    if not review_elements:
        print(f"No reviews found on page: {url}")
        return []

    reviews = []
    for review in review_elements:
        r_title_element = review.select_one("a[data-hook='review-title']")
        r_title = r_title_element.text.strip() if r_title_element else None

        r_content_elements = review.select_one("span[data-hook='review-body']")
        r_content = r_content_elements.text.strip() if r_content_elements else None

        r_verified_element = review.select_one("span[data-hook='avp-badge']")
        r_verified = r_verified_element.text.strip() if r_verified_element else None

        review_data = {
            "title": r_title,
            "content": r_content,
            "verified": r_verified,
        }
        reviews.append(review_data)

    return reviews

def get_all_reviews(base_review_url, max_pages=5):
    """
    Scrapes reviews from multiple pages of Amazon reviews.
    """
    all_reviews = []
    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}...")
        url = f"{base_review_url}&pageNumber={page}"  # Construct URL with current page number
        reviews = get_reviews_from_page(url)

        if not reviews:  # Stop if no reviews are found
            print(f"No reviews found on page {page}. Stopping.")
            break

        all_reviews.extend(reviews)
        time.sleep(2)  

    return all_reviews
