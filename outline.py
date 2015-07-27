"""
Timetable:
Start - Finish  ; Date   ; Work / Notes

11:00 - 12:30 PM; 7/12/15; Meeting and Discussion
12:00 - 01:00 PM; 7/15/15; Research
04:30 - 05:15 PM; 7/16/15; Outline / Research / Setup
01:30 - 02:30 PM; 7/17/15; Setup / Testing
01:00 - 03:00 PM; 7/19/15; Setup / Testing / Base Code (~50% of foundational code)
03:10 - 04:35 PM; 7/20/15; Base Code (most foundational code, primative and incomplete functionality)
01:30 - 03:30 PM; 7/23/15; Base Code (general functionality achieved, added dispersion plot)
01:05 - 03:15 PM; 7/24/15; Base Code (1.0 functionality, includes all excel data)
10:30 - 12:00 PM; 7/27/15; Meeting and Discussion

Total time:  mins ->  hours  minutes

Current issues:
program will not continue until dispersion plot is exited, redo UI here
related words auto-prints in inconistant format
synonyms need work, as do antonyms (maybe add second degree words)


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




"""
