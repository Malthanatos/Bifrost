"""
Current issues:
program will not continue until dispersion plot is exited, redo UI here
program will only display dispersion fo one word at a time in mwac
related words auto-prints in inconistant format
synonyms need work, as do antonyms (maybe add second degree words)

fix the excel output to not ask for a file when using off-use commands
add option to save certain lists of words (helpful)
excel file opening can be sped up and save memeory using openpyxl,
    but this is problematic to implement, work on this in excel_test.py
program crahses when: sorting is set to non-default, output is both or excel, dtree is called

get mindep and polys for large input to excel
check google ngrams and try to use the raw data
get mindep and dtree to work with most common word, print the
    parts of speech and ask which one to work with
    ie: when using mindep return one for each part of speech (the first)


Needs to:

Interface:

User Interface (text):
    ask for a word and/or a textual refrence (corpus)
    ask what to do with it
    UI -> functionality
    functionality -> UI
    list of requested information
    (in a formated manner)
    ask for another word

User Interface (graphical):
    in GUI:
        inputs:
            word, corpus, order results by ?, plot?, 
        outputs:
            definition, occurences, TASA, list of related words / synonyms / antonyms
            may need to order variable length outputs by a given value

Functionality:

NTLK:
    given a word:
        find similar words
        number of occurences and list them
        plot the dispersion of the word
    
WordNet:
    given a word:
        return definition, synonyms, antonyms, related words, etc.

TASA:
    given a word:
        return the TASA number (age of appropriateness)

General:
    Be able to rank results by a particular value or type of value

second stage:
    min depth, hyponym tree, correlate, database of words with > 1 frequency
    focus on first definition
    create excel file using many inputs
    use aoa.rating.mean and std-dev, subtlex.wf - log_10(cd), zeno.sfi and d
    keep track of number of pos type definitions

    add simple support to add new corpus

https://github.com/nltk/nltk/wiki/Adding-a-Corpus


"""
