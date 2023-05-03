# Requires wget!

import os

DEBUG = True

languages = input("Name of languages (split by commas): ").lower()
languages = languages.split(",")

for language in languages:
    title = language.title()
    title2 = title.replace(" ", "") # No space in second title
    language = language.replace(" ", "_") # Don't allow spaces

    if DEBUG:
        print(f"language = '{language}'")
        print(f"title = '{title}'")

    os.system(f"cd ./raw-dictionaries/ && wget \
\"https://kaikki.org/dictionary/{title}/all-senses/kaikki_dot_org-dictionary-\
{title2}-all-senses.json\" -O \"{language}.json\"")
