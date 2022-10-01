import json

dictionaries = [
    ["Ancient Greek", "ancient_greek.json"],
    ["Latin", "latin.json"],
    ["Old Norse", "old_norse.json"],
    ["Old English", "old_english.json"],
    ["Middle English", "middle_english.json"],
    ["Old French", "old_french.json"],
    ["Middle French", "middle_french.json"],
]

while True:
    print("Choose language:")

    for i, d in enumerate(dictionaries):
        print(f"[{i}] {d[0]}")

    language = int(input("Language >> "))
    language_path = dictionaries[language][1]

    words = {}

    with open(f"./dictionaries/{language_path}", "r") as f:
        words = json.load(f)
    
    print("Type ':back' to select languages")

    while True:
        en_word = input("English word: ")

        if en_word == ":back":
            break

        matches = []
        
        for definition, word in words.items():
            if en_word in definition:
                matches.append(f"{bytes(word, 'utf-8').decode('unicode-escape')} - {str(definition)}")
        
        print(f"Results:\n")
        for result in matches:
        #     result = bytes(result, "utf-8")
        #     print(result.decode("unicode-escape"))
            print(result)
        print()