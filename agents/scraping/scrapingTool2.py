import wikipedia
import wikipediaapi


def wiki_search(kword):
    """
    Search Wikipedia for a keyword and fetch the content of the best-matched page along with related links.
    :param kword: The search term to look up.
    :return: A dictionary with 'content' and 'related_links'.
    """
    try:
        search_results = wikipedia.search(kword)
        if not search_results:
            return {
                "error": f"No results found for '{kword}'. Please try another keyword."
            }

        best_match = search_results[0]
        print(f"Best match for '{kword}': {best_match}")

        wiki_wiki = wikipediaapi.Wikipedia(
            language="en",
            user_agent="WikiSearch (nvujic2002@gmail.com)"
        )

        page = wiki_wiki.page(best_match)

        if page.exists():
            content = page.text

            related_links = []
            for link_title in page.links.keys():
                related_links.append(f"https://en.wikipedia.org/wiki/{link_title.replace(' ', '_')}")
                if len(related_links) >= 50:  # how many links to fetch
                    break

            return {
                "content": content,
                "related_links": related_links
            }
        else:
            return {
                "error": f"The page for '{best_match}' does not exist or is inaccessible."
            }

    except Exception as e:
        return {
            "error": f"An error occurred: {e}"
        }


if __name__ == "__main__":
    keyword = input("Enter a Wikipedia keyword to scrape: ")
    result = wiki_search(keyword)

    print("______________________________________________")
    if "error" in result:
        print("Error:", result["error"])
    else:
        print("_________________Content______________________")
        print(result["content"])
        print("\n_______________Related Links__________________")
        for i, link in enumerate(result["related_links"], start=1):
            print(f"{i}. {link}")
