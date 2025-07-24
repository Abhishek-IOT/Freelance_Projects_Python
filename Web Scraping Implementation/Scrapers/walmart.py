from playwright.sync_api import sync_playwright
import pandas as pd
import json

def scrape_walmart():
    urls = [
        "https://www.walmart.com/ip/onn-Android-TV-4K-UHD-Streaming-Device/493824815"
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

                product_name = "N/A"
                rating = "N/A"
                review_count = "N/A"
                offers_text = "None"

                # Try getting embedded JSON-LD metadata
                scripts = page.query_selector_all('script[type="application/ld+json"]')
                for script in scripts:
                    content = script.inner_text()
                    if '"@type":"Product"' in content:
                        product_data = json.loads(content)

                        product_name = product_data.get("name", "N/A")
                        rating = product_data.get("aggregateRating", {}).get("ratingValue", "N/A")
                        review_count = product_data.get("aggregateRating", {}).get("reviewCount", "N/A")
                        break

                # Check for subscriptions
                body_text = page.inner_text("body")
                matched_offers = [offer for offer in subscription_keywords if offer.lower() in body_text.lower()]
                offers_text = ", ".join(matched_offers) if matched_offers else "None"

                data.append({
                    "Product Name": product_name,
                    "Rating": rating,
                    "Number of Reviews": review_count,
                    "Subscription Offers": offers_text,
                    "Product URL": url
                })

            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

        browser.close()

    df = pd.DataFrame(data)
    df.to_excel("walmart_products.xlsx", index=False)
    print("✅ Data saved to walmart_products.xlsx")

# To run directly
if __name__ == "__main__":
    scrape_walmart()
