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
* The entire `dictionaries/` folder is approximately 81MB, so if space is a
concern, do not download this.

## Usage
Simply run this to start:

```bash
python translator.py
```

## Built-in languages
### Modern
* Spanish
* Italian
* German
* Russian
* Portuguese
* Polish
* French
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
* Sumerian (Busted)
* Tocharian B

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
