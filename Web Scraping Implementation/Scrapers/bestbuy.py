from playwright.sync_api import sync_playwright
import pandas as pd

def scrape_bestbuy():
    urls = [
        "https://www.bestbuy.com/site/sony-65-class-bravia-xr-a80l-oled-4k-uhd-smart-google-tv/6530758.p"
    ]

    subscription_keywords = [
        "YouTube Premium", "Apple TV+", "SiriusXM", "Xbox Game Pass", "Fubo TV"
    ]

    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()

        for url in urls:
            try:
                print(f"Scraping: {url}")
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(3000)

                # Product name
                title_elem = page.query_selector("h1")
                product_name = title_elem.inner_text().strip() if title_elem else "N/A"

                # Ratings and review count
                rating_elem = page.query_selector("div.c-reviews > div > p")
                rating_text = rating_elem.inner_text().strip() if rating_elem else "N/A"

                review_count_elem = page.query_selector("span.c-reviews-v4__count")
                review_count = review_count_elem.inner_text().strip() if review_count_elem else "N/A"

                # Full page text for subscription keyword match
                body_text = page.inner_text("body")
                matched_offers = [offer for offer in subscription_keywords if offer.lower() in body_text.lower()]
                offers_text = ", ".join(matched_offers) if matched_offers else "None"

                data.append({
                    "Product Name": product_name,
                    "Rating": rating_text,
                    "Number of Reviews": review_count,
                    "Subscription Offers": offers_text,
                    "Product URL": url
                })

            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

        browser.close()

    # Save to Excel or CSV
    df = pd.DataFrame(data)
    df.to_excel("bestbuy_products.xlsx", index=False)
    print("✅ Data saved to bestbuy_products.xlsx")

# To run directly
if __name__ == "__main__":
    scrape_bestbuy()
