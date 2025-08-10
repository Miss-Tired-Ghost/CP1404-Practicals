"""
Wikipedia Page Searcher
Code By: April First/Miss Ghost
"""

import wikipedia
from warnings import catch_warnings

title = input("Enter page title: ")
while title:
    with catch_warnings(action="ignore"):
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.PageError:
            print(f"Page id \"{title}\" does not match any pages. Try another id!")
        except wikipedia.exceptions.DisambiguationError as DisambiguationError:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(DisambiguationError.options)
    title = input("Page title or search phrase: ")
print("Thank you.")



