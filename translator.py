import json
import re
import codecs
from os import listdir
from os.path import isfile, join

dict_dir = "./dictionaries"

files = [] #[f for f in listdir(directory) if isfile(join(directory, f))]
for f in listdir(dict_dir):
    if isfile(join(dict_dir, f)):
        if f.endswith(".json"):
            files.append(f)

files.sort()

dictionaries = []
for file in files:
    file_name = file[:-5]
    file_name = file_name.replace("_", " ")
    dictionaries.append([file_name.title(), f"{file}"])

def print_help():
    print("\nType ':back' or ':b' to go back to selecting languages")
    print("Type ':quit' or ':q' to quit")
    print("Start word with '=' for exact matches (words better for single words)")
    print("Start word with '?' if you encounter an encoding error")

def javascript_to_python_unicode(js_unicode: str):
    js_unicode = bytes(temp, "utf-8").decode("unicode_escape") # Turn \\ into \, but it's sitll a Javascript unicode
    js_unicode = json.dumps({"convert": js_unicode})
    js_unicode = json.loads(js_unicode)["convert"]
    return js_unicode

while True:
    print("Type ':quit' or ':q' to quit")
    print("Choose a language:")

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
    
    print_help()
    
    while True:
        print("Type ':h' or 'help' for help")
        en_word = input("English word: ")

        strict = False
        unicode_mode = True

        if en_word == ":back" or en_word == ":b":
            break
        elif en_word == "":
            continue
        elif en_word[0] == "=": # Exact match
            strict = True
            en_word = en_word[1:]
        elif en_word == ":q" or en_word == ":quit":
            quit()
        elif en_word == ":h" or en_word == ":help":
            print_help()
            continue
        elif en_word[0] == "?": # Unicode error
            unicode_mode = False
            en_word = en_word[1:]

        matches = []
        
        if strict:
            for definition, d_words in words.items():
                for d_word in d_words:
                    d_word_real = d_word[0]
                    d_word_pos = d_word[1]

                    for dd_word in re.split("[,.!?;() ]", definition):
                        if en_word == dd_word:
                            temp = d_word_real[1:-1] # Get rid of surrounding quotes
                            temp = javascript_to_python_unicode(temp)

                            matches.append(f"({str(d_word_pos)[1:-1]}) \"{temp}\" - {str(definition)}")
        else:
            for definition, d_words in words.items():
                for d_word in d_words:
                    d_word_real = d_word[0]
                    d_word_pos = d_word[1]
                    
                    if en_word in definition:
                        temp = d_word_real[1:-1] # Get rid of surrounding quotes
                        temp = javascript_to_python_unicode(temp)

                        matches.append(f"({str(d_word_pos)[1:-1]}) \"{temp}\" - {str(definition)}")
        
        matches.sort()
        
        print(f"Results:\n")
        for result in matches:
            try:
                print(result)
            except Exception as e:
                print(f"!!! error !!!\t:\t{e}")
        print()