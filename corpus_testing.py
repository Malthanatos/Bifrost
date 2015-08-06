# Corpus Testing
# Author :      Nathan Krueger
# Created       10:45 PM 8/3/15
# Last Updated  00:00 PM 8/0/15
# Version       0.1

import nltk, re, pprint
from nltk import word_tokenize
from urllib import request

def from_web()->None:
    #normal .txt or raw interaction
    url = 'http://www.guteberg.org/files/2554/2554.txt'
    response = request.urlopen(url)
    raw = response.read().decode('utf8')
    type(raw) #->str
    len(raw) #->in letters/symbols
    raw[:75] #->the first 76 characters
    tokens = word_tokenize(raw)
    #returns a list
    tokens[:10] #-> first 11 tokens in a list
    text = nlrk.Text(tokens)
    text[1024:1062] #->a small excerpt from this location by tokens
    text.collocations() #->groups of 2 words that often appear next
    #to each other (groups seperated by ';'
    raw.find('Part 1') #-> index of P
    raw.rfind("Part 1") #-> index of 1 (reverse find, find last value's index)

    #HTML interaction
    url = 'http://news.bbc.co.uk/2/hi/health/2284783.stm'
    html = request.urlopen(url).read.decode('utf8')
    #returns html coded text
    #using Beautiful Soup library we can convert HTML to raw text
    #Note: the character '|' is often used to replace formatting differences
    #from bs4 import BeautifulSoup as BS
    #raw = BS(html).get_text()
    raw = nltk.clean_html(html) #->removes formatting, requires installing BS
    tokens = word_tokenize(raw)
    text = nltk.Text(tokens)
    text.concordence('gene') #-> list of all occurences of the word gene
    #centered around ~100 character context
    return

def local_text()->None:
    try:
        f = open('corpora.txt')
        raw = f.read()
    except (IOError):
        print("File does not exist in current directory")
    tokens = word_tokenize(raw)
    words = [w.lower() for w in tokens]
    vocab = sorted(set(words))
    
    return


local_text()
