import json
import re

# dictionaries = [
#     # MODERN LANGUAGES
#     ["Spanish", "spanish.json"],
#     ["Italian", "italian.json"],
#     ["German", "german.json"],
#     ["Russian", "russian.json"],
#     ["Portuguese", "portuguese.json"],
#     ["Polish", "polish.json"],
#     ["French", "french.json"],
    
#     # SUPPOSED MODERN LANGUAGES
#     ["Latin", "latin.json"],

#     # HISTORICAL/ANCIENT LANGUAGES
#     ["Ancient Greek", "ancient_greek.json"],
#     ["Middle English", "middle_english.json"],
#     ["Old English (Anglo-Saxon)", "old_english.json"],
#     ["Old Armenian", "old_armenian.json"],
#     ["Middle French", "middle_french.json"],
#     ["Old French", "old_french.json"],
#     ["Old Saxon", "old_saxon.json"],
#     ["Old High German", "old_high_german.json"],
#     ["Old Norse", "old_norse.json"],
#     ["Old Swedish", "old_swedish.json"],
#     ["Classical Syriac", "classical_syriac.json"],
#     ["Middle Irish", "middle_irish.json"],
#     ["Old Irish", "old_irish.json"],
#     ["Middle Dutch", "middle_dutch.json"],
#     ["Old Church Slavonic", "old_church_slavonic.json"],
#     ["Akkadian", "akkadian.json"],
#     ["Sumerian (busted)", "sumerian.json"], # UNICODE ERRRORS
#     ["Aramaic", "aramaic.json"],
#     ["Latin2", "latin2.json"],
# ]

from os import listdir
from os.path import isfile, join

dict_dir = "./dictionaries"

files = [] #[f for f in listdir(directory) if isfile(join(directory, f))]
for f in listdir(dict_dir):
    if isfile(join(dict_dir, f)):
        if f.endswith(".json"):
            files.append(f)

dictionaries = []
for file in files:
    file_name = file[:-5]
    file_name = file_name.replace("_", " ")
    dictionaries.append([file_name.title(), f"{file}"])

while True:
    print("Type ':quit' or ':q' to quit")
    print("Choose a language:")

    for i, d in enumerate(dictionaries):
        # if i == 0:
        #     print("[[Modern Languages]]")
        # elif i == 7:
        #     print("\n[[Revived]]")
        # elif i == 8:
        #     print("\n[[Ancient Languages]]")
        print(f"[{i}] {d[0]}")

    language = input("Language >> ")
    if language == ":quit" or language == ":q":
        print("Goodbye!")
        break
    
    language_no = int(language)
    language_path = dictionaries[language_no][1]

    words = {}

    with open(f"./dictionaries/{language_path}", "r") as f:
        words = json.load(f)
    
    while True:
        # en_word = input("English word: ")
        print("Type ':back' or ':b' to go back to selecting languages")
        print("Type ':quit' or ':q' to quit")
        print("Start word with '=' for exact matches")
        en_word = input("English word: ")

        strict = False

        if en_word == ":back" or en_word == ":b":
            break
        elif en_word == "":
            continue
        elif en_word[0] == "=": # Exact match
            strict = True
            en_word = en_word[1:]
        elif en_word == ":q" or en_word == ":quit":
            quit()

        matches = []
        
        if strict:
            for definition, d_words in words.items():
                for d_word in d_words:
                    # Dict 2.0 structure
                    d_word_real = d_word[0]
                    d_word_pos = d_word[1]

                    for dd_word in re.split("[,.!?;() ]", definition):
                        if en_word == dd_word:
                            matches.append(f"({str(d_word_pos)[1:-1]}) {bytes(d_word_real, 'utf-8').decode('unicode-escape', 'replace')} - {str(definition)}")
        else:
            for definition, d_words in words.items():
                for d_word in d_words:
                    # Dict 2.0 structure
                    d_word_real = d_word[0]
                    d_word_pos = d_word[1]
                    
                    if en_word in definition:
                        matches.append(f"({str(d_word_pos)[1:-1]}) {bytes(d_word_real, 'utf-8').decode('unicode-escape', 'replace')} - {str(definition)}")
        
        matches.sort()
        
        print(f"Results:\n")
        for result in matches:
        #     result = bytes(result, "utf-8")
        #     print(result.decode("unicode-escape"))
            try:
                print(result)
            except Exception as e:
                print(f"!!! error !!!\t:\t{e}")
        print()