import json
import re

dictionaries = [
    ["Ancient Greek", "ancient_greek.json"],
    ["Latin", "latin.json"],
    ["Old Norse", "old_norse.json"],
    ["Old English", "old_english.json"],
    ["Middle English", "middle_english.json"],
    ["Old French", "old_french.json"],
    ["Middle French", "middle_french.json"],
    ["French", "french.json"],
    ["Old High German", "old_high_german.json"],
    ["Old Irish", "old_irish.json"],
    ["Middle Irish", "middle_irish.json"],
    ["Old Church Slavonic", "old_church_slavonic.json"],
    ["Russian", "Russian.json"],
]

while True:
    print("Type ':quit' or ':q' to quit")
    print("Choose language:")

    for i, d in enumerate(dictionaries):
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

        matches = []
        
        if strict:
            for definition, d_words in words.items():
                for d_word in d_words:
                    for dd_word in re.split("[,.!?; ]", definition):
                        if en_word == dd_word:
                            matches.append(f"{bytes(d_word, 'utf-8').decode('unicode-escape')} - {str(definition)}")
        else:
            for definition, d_words in words.items():
                for d_word in d_words:
                    if en_word in definition:
                        matches.append(f"{bytes(d_word, 'utf-8').decode('unicode-escape')} - {str(definition)}")
        
        print(f"Results:\n")
        for result in matches:
        #     result = bytes(result, "utf-8")
        #     print(result.decode("unicode-escape"))
            try:
                print(result)
            except Exception as e:
                print(f"!!! error !!!\t:\t{e}")
        print()