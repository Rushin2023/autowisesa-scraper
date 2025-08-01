
import requests
from bs4 import BeautifulSoup
import json

def fetch_webuycars():
    url = "https://www.webuycars.co.za/buy-a-car"
    headers = {"User-Agent": "Mozilla/5.0"}
    listings = []

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for card in soup.select("div.card-body")[:10]:
                title = card.find("h2")
                price = card.find("div", class_="price")
                link = card.find("a", href=True)
                if title and price and link:
                    listings.append({
                        "title": title.text.strip(),
                        "price": price.text.strip(),
                        "link": f"https://www.webuycars.co.za{link['href']}"
                    })
    except Exception as e:
        listings.append({"error": str(e)})

    return listings

if __name__ == "__main__":
    data = fetch_webuycars()
    print(json.dumps(data, indent=2))
