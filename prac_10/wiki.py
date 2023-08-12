import wikipedia
search_phrase = input("Enter a search phrase/page title (press enter to exit): ")
while search_phrase != "":
    try:
        page = wikipedia.page(search_phrase)  # autosuggest did not work
        print("\nTitle:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)

    except wikipedia.exceptions.DisambiguationError as e:
        print("DisambiguationError: The search term is ambiguous. Please provide more specific input.")

    search_phrase = input("Enter a search phrase/page title (press enter to exit): ")

