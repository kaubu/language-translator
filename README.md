# language-translator
Search through the definitions for many different languages, including ancient
languages.

## IMPORTANT NOTES!!!
* This uses sources from Wiktionary, which:
    1. May not be entirely accurate, and
    2. May not include all possible words
* Rather than translating entire sentences, this looks up one word or phrase
at a time. Funtionality is planned in the future to search entire sentences,
split and tokenize them, then return the results.
* The entire `dictionaries/` folder is approximately 92MB, so if space is a
concern, do not download that directory.

## Usage
Simply run this to start:

```bash
python translator.py
```

## Add a language
### Pre-built
1. Download a language from https://kaikki.org/dictionary/, and put the 
resulting file in the `raw-dictionaries/` directory. For all the pre-packaged
dictionaries, I did use the "Non-inflected, non-alternative" word senses, but have now used the All senses
JSON file.
2. Change the file name to end in `.json`. For a more aesthetically pleasing
listing in the languages list, change the file name to just its language name,
e.g. change `kaikki.org-dictionary-Arabic-all-no-YVQKzm` -> `arabic.json`.
3. Run `python serializer.py`, and select either **Manual installation** (for
converting one dictionary at a time) or **Serialize all .json files in a**
**directory** to convert every .json file in that directory.
4. You're done. Once the conversion has finished, it will automatically be
listed in the `translator.py` program once run.
### Manually
If a language is not already made on that website, such as Proto-Indo-European,
you can follow these steps.

**TODO**
<!-- 1. Download the  -->

## Built-in languages
### Proto-Languages
* Proto-Indo-European
### Modern
* Spanish
* Italian
* German
* Russian
* Portuguese
* Polish
* French
* Japanese
* Arabic
### Revived
* Latin
### Ancient
* Ancient Greek
* Middle English
* Old English (Anglo-Saxon)
* Old Armenian
* Middle French
* Old French
* Old Saxon
* Old High German
* Old Norse
* Old Swedish
* Classical Syriac
* Middle Irish
* Old Irish
* Middle Dutch
* Old Church Slavonic
* Akkadian
* Aramaic
* Coptic
* Egyptian
* Gothic
* Sanskrit
* Sumerian
* Tocharian B
### IAL/Conlangs
* Esperanto
* Ido

## Misc. Notes
### Verbs
Most Latin verbs start with "I" as in "I like". Some Latin verbs start with
"to" like "to hate".

Some other languages don't have verbs in the "to VERB" format, and just have
the plain verb.

## Credits
Credits to https://kaikki.org/, which supplied the majority of this codebase,
from the mining of Wiktionary to sorting it out. I only coded this program
which sorts through that data.
