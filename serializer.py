import json
import re

DEBUG = False

print("""What mode do you want to use?
[1] Manual serialization (raw glosses only, recommended)
[2] Manual serialization (all glosses, full of duplicates)
[3] Serialize all .json files in a directory""")

mode = input("\n>> ")

# For All non-inflected, non-alternative word senses
def serialize_file_raw(dictionary_path, new_file_name):
    words = {}

    with open(dictionary_path, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)

            if DEBUG:
                print(json.dumps(data, indent=2, sort_keys=True))
                input("Continue? ")
            
            try:
                word = json.dumps(data["word"])
                pos = json.dumps(data["pos"]) # Part of Speech
            except Exception as e:
                if DEBUG: print(f"lvl 1 error: {e}")
                continue # No word or parts of speech
            
            for sense in data["senses"]:
                try:
                    dict_key = str(sense["raw_glosses"][0])
                    
                except Exception as e:
                    try:
                        dict_key = str(sense["glosses"][0])

                    except Exception as e:
                        if DEBUG: print(f"lvl 3 error: {e}")
                        continue

                    if DEBUG: print(f"lvl 2 error: {e}")
                
                # Replace common error with fix
                key = re.sub("\[string \"Module\:Quotations\"\]\:118\: Please specify a language code in the first parameter\. The value \"(.*)\" is not valid. See Wiktionary:List of languages.", "(\\1)", dict_key)

                if key in words:
                    words[key].append([word, pos])
                else:
                    words[key] = [[word, pos]] # Index is search term, key is word
    
    # # Get rid of duplicate entries
    # for definition in words.keys():
    #     print(f"definition = {definition}")
    #     # print(f"d_words = {d_words}")
    #     input("Continue?")

    #     for word in words[definition]:
    #         print(f"word = {word}")
    #         input("| Continue?")

    with open(f"./dictionaries/{new_file_name}", "w") as f:
        f.write(json.dumps(words, sort_keys=True))

# For All word senses
def serialize_file(dictionary_path, new_file_name):
    words = {}

    with open(dictionary_path, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)

            if DEBUG:
                print(json.dumps(data, indent=2, sort_keys=True))
                input("Continue? ")
            
            try:
                word = json.dumps(data["word"])
                pos = json.dumps(data["pos"]) # Part of Speech
            except:
                continue # No word or parts of speech
            
            for sense in data["senses"]:
                try:
                    # Raw glosses first
                    dict_key = str(sense["raw_glosses"][0])

                    # Replace common error with fix
                    key = re.sub("\[string \"Module\:Quotations\"\]\:118\: Please specify a language code in the first parameter\. The value \"(.*)\" is not valid. See Wiktionary:List of languages.", "(\\1)", dict_key)

                    if key in words:
                        words[key].append([word, pos])
                    else:
                        words[key] = [[word, pos]] # Index is search term, key is word

                except:
                    pass
                
                try:
                    # Normal glosses too
                    dict_key = str(sense["glosses"][0])

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

if mode == "1" or mode == "2":
    print("Type :q to quit")

    while True:
        file_name = input('Name of the .json file (without the .json bit): ')

        if file_name == ":q":
            break

        dictionary_path = f"./raw-dictionaries/{file_name}.json"

        if mode == "1": serialize_file_raw(dictionary_path, f"{file_name}.json")
        elif mode == "2":
            serialize_file(dictionary_path, f"{file_name}.json")
    
        print("Serialization complete!")

elif mode == "3":
    from os import listdir
    from os.path import isfile, join

    directory = input("Directory [./raw-dictionaries]: ")
    if directory == "": directory = "./raw-dictionaries"

    files = []
    for f in listdir(directory):
        if isfile(join(directory, f)):
            if f.endswith(".json"):
                files.append(f)
    
    files = sorted(files) # Sort them alphabetically

    for file in files:
        print(f"Serializing '{file}'...")
        serialize_file_raw(f"{directory}/{file}", file)
        print("Serializing done!")
else:
    print("Not a mode")