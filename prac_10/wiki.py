import wikipedia


def main():
    """Ask for a search phrase from the user and display the wikipedia title, url and summary."""
    search_phrase = input("Search phrase: ")
    while search_phrase != "":
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(f"Title: {page.title}")
            print(f"URL: {page.url}")
            print(wikipedia.summary(search_phrase))
        except wikipedia.exceptions.DisambiguationError:
            print("This page is a disambiguation page.")
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        search_phrase = input("Search phrase: ")


main()
