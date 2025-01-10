import requests
from bs4 import BeautifulSoup

def scrape_wiki_from_url(url):
    """
    Scrape Wikipedia article for a given URL.
    :param url: The URL of the Wikipedia page.
    :return: Article content as plain text.
    """
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("Scraping:" + url)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            content = " ".join([p.text for p in paragraphs])

            return content.strip()
        else:
            return f"Error fetching wiki article from {url}.\nStatus code: {response.status_code}"
    except Exception as e:
        return f"Error fetching wiki article from {url}.\nException: {e}"

if __name__ == '__main__':
    urls = [
        input("Enter Wikipedia URL 1: "),
        input("Enter Wikipedia URL 2: "),
        input("Enter Wikipedia URL 3: ")
    ]

    for i, url in enumerate(urls, start=1):
        content = scrape_wiki_from_url(url)
        print(f"\n________Content of Link {i}________")
        print(content)
