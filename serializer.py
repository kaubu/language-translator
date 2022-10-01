# OLD_NORSE = "./raw-dictionaries/kaikki.org-dictionary-OldNorse-all--NmoVhv-non_inflected-non_alternative.json"

import json

words = {}

with open(f"./raw-dictionaries/{input('JSON raw file path: ./raw-dictionaries/')}", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        # print(data["word"])
        if "word" in data:
            word = str(data["word"])
        else:
            continue
        
        if word in words: # If there already exists an entry, skip it
            continue
        else:
            # words.append(word: data)
            for sense in data["senses"]:
                # print(json.dumps(sense["raw_glosses"], indent=2, sort_keys=True))
                # input("Next raw gloss?")

                try:
                    dict_key = str(sense["raw_glosses"][0])
                    # print(f"debug: dict_key = '{dict_key}'")

                    words[dict_key] = json.dumps(data["word"]) # Index is search term, key is word
                except:
                    continue

# while True:
#     # Find a word
#     word = input("ON Word: ")
#     print(json.dumps(words[word], indent=2, sort_keys=True))

with open(f"./dictionaries/{input('JSON export file path: ./dictionaries/')}", "w") as f:
    f.write(json.dumps(words, sort_keys=True))

# Find a word
# while False:
#     en_word = input("English word: ")

#     matches = []
    
#     for definition, word in words.items():
#         if en_word in definition:
#             matches.append(f"{bytes(word, 'utf-8').decode('unicode-escape')} - {str(definition)}")
    
#     print(f"Results:\n")
#     for result in matches:
#     #     result = bytes(result, "utf-8")
#     #     print(result.decode("unicode-escape"))
#         print(result)
#     print()