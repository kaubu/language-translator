# Requires wget!

import os

DEBUG = True

# Default download list:
# akkadian,ancient greek,arabic,aramaic,basque,breton,classical syriac,coptic,egyptian,esperanto,finnish,french,german,gothic,hebrew,icelandic,ido,interlingua,irish,italian,japanese,latin,lithuanian,middle_english,middle french,middle irish,old church slavonic,old english,old french,old high german,old irish,old norse,old polish,persian,polish,portugese,proto-brythonic,proto-celtic,proto-finnic,proto-germanic,proto-indo-european,proto-indo-iranian,proto-italic,proto-slavic,proto-west germanic,russian,sanskrit,scots,scottish gaelic,spanish,sumerian,tocharian b,ugratic,welsh,west frisian,yiddish

languages = input("Name of languages (split by commas): ").lower()
languages = languages.split(",")

for language in languages:
    title = language.title()
    title2 = title.replace(" ", "") # No space in second title

    # They changed how the files are represented
    # if "Indo-" in title2: title2 = title2.replace("Indo-")
    # if "Proto-" in title2: title2 = title2.replace("Proto-", "Proto")
    if "_" in title: title = title.replace("_", " ")
    # if "-" in title: title = title.replace("-", "")
    if "-" in title2: title2 = title2.replace("-", "")
    if "_" in title2: title2 = title2.replace("_", "")
    # Middle English exception
    if "Middle English" in title2:
        title2 = title2.replace("Middle ", "Middle")

    language = language.replace(" ", "_") # Don't allow spaces

    if DEBUG:
        print(f"language = '{language}'")
        print(f"title = '{title}'")
        print(f"title2 = '{title2}'")

    os.system(f"cd ./raw-dictionaries/ && wget \
\"https://kaikki.org/dictionary/{title}/all-senses/kaikki_dot_org-dictionary-\
{title2}-all-senses.json\" -O \"{language}.json\"")
