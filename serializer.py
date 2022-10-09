import json
import re

debug = False

print("""What mode do you want to use?
[1] Manual serialization
[2] Serialize all .json files in a directory""")

mode = input("\n>> ")

def serialize_file(dictionary_path, new_file_name):
    words = {}

    with open(dictionary_path, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)

            if debug:
                print(json.dumps(data, indent=2, sort_keys=True))
                input("Continue? ")
            
            word = json.dumps(data["word"])
            pos = json.dumps(data["pos"]) # Part of Speech
            
            for sense in data["senses"]:
                try:
                    dict_key = str(sense["raw_glosses"][0])

                    # Replace common error with fix
                    key = re.sub("\[string \"Module\:Quotations\"\]\:118\: Please specify a language code in the first parameter\. The value \"(.*)\" is not valid. See Wiktionary:List of languages.", "(\\1)", dict_key)

                    if key in words:
                        words[key].append([word, pos])
                    else:
                        words[key] = [[word, pos]] # Index is search term, key is word
                except:
                    continue

    with open(f"./dictionaries/{new_file_name}", "w") as f:
        f.write(json.dumps(words, sort_keys=True))


if mode == "1":
    print("Type :q to quit")

    while True:
        file_name = input('Name of the .json file (without the .json bit): ')

        if file_name == ":q":
            break

        dictionary_path = f"./raw-dictionaries/{file_name}.json"

        serialize_file(dictionary_path, f"{file_name}.json")

elif mode == "2":
    from os import listdir
    from os.path import isfile, join

    directory = input("Directory [./raw-dictionaries]: ")
    if directory == "": directory = "./raw-dictionaries"

    files = []
    for f in listdir(directory):
        if isfile(join(directory, f)):
            if f.endswith(".json"):
                files.append(f)

    for file in files:
        print(f"Serializing '{file}'...")
        serialize_file(f"{directory}/{file}", file)
        print("Serializing done!")
else:
    print("Not a mode")