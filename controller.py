# Controller
# Author :      Nathan Krueger
# Created       5:00 PM 7/16/15
# Last Updated  3:10 PM 7/24/15
# Version       1.0

import UI#, GUI
import nltk
import xlrd
import xlwt
from nltk.book import *
from nltk.corpus import wordnet

#global variable declarations:
word = ''
corpus = ''
aoa = ''
awl = ''
subtlex = ''
tasa = ''
zeno = ''

#Note: excel coords act as follows:
#cell(0,0) -> A-1   and cell(1,10) -> B-11

def run()->None:
    """Initializes program"""
    global corpus
    excel_setup()
    corpus, word = UI.setup()
    corpus = eval(corpus)
    #print('hello')
    #print(corpus)
    UI.return_data(analyze(word))
    #print('goodbye')
    return

def excel_setup()->None:
    """opens the necessary files/worksheets from excel documents"""
    global aoa, awl, subtlex, tasa, zeno
    #open files
    aoa = xlrd.open_workbook('AoA.xlsx')
    awl = xlrd.open_workbook('AWL.xls')
    subtlex = xlrd.open_workbook('SUBTLEX.xlsx')
    tasa = xlrd.open_workbook('tasa.xlsx')
    zeno = xlrd.open_workbook('Zeno.xlsx')
    #open worksheets
    aoa = aoa.sheet_by_index(0)
    awl = awl.sheet_by_index(0)
    subtlex = subtlex.sheet_by_index(0)
    tasa = tasa.sheet_by_index(0)
    zeno = zeno.sheet_by_index(0)
    return

def contents(file: str)->[str]:
    """returns a list of the contents of the given file"""
    result = []
    return result

def analyze(word: str)->[str]:
    """analyze a given word and report all available data"""
    result = [[],[],[]]
    #nltk analysis
    result[0] = nltk_data(word)
    #wordnet analysis
    result[1] = wordnet_data(word)
    #excel analysis
    result[2] = excel_data(word)
    return result

def nltk_data(word: str)->[str]:
    """returns a list of semi-formatted nltk word data"""
    #similar words, occurences, frequency plot
    result = [None,None,None,None,None]
    #similar seems to auto-print and return None
    #technically part of UI:
    print("\nRelated words within selected corpus: ")
    corpus.similar(word)
    result[0] = len(corpus)
    result[1] = len(set(corpus))
    result[2] = result[1] / result[0]
    result[3] = corpus.count(word)
    result[4] = 100 * result[3] / result[0]
    #see UI for more specifics here:
    try:
        print("Word's distribution within the corpus: (see second window)")
        print("\nNote: in current development stage the program cannot continue until the \nfrequency distribution window is closed.")
        corpus.dispersion_plot([word])
    except (ValueError, ImportError):
        print("\nMatplot and/or numpy libraries are not installed, frequecny distribution cannot be displayed")
    except(...):
        print("An unknown error occured while attempting to display the word's frequency distribution")
    return result

def wordnet_data(word: str)->[str]:
    """returns a list of semi-formatted wordnet word data"""
    #definitions, parts of speech, synonyms, antonyms, related words
    result = [[],[],[],set(),[],[]]
    word_info = wordnet.synsets(word)
    if (len(word_info) > 0):
        word_info = word_info[0]
    else:
        return result
    lemmas = wordnet.lemmas(word)
    for synset in wordnet.synsets(word):
        result[0].append(synset.definition())
        result[1].append(synset.pos())
        #how to access part of speech?
    result[2] = word_info.lemma_names()
    for lemma in lemmas:
        for word in lemma.antonyms():
            result[3].add(word.name())
    result[4] = (word.name().split('.')[0] for word in word_info.hyponyms())
    result[5] = (word.name().split('.')[0] for word in word_info.hypernyms())
    #how to find similar words? Doesn't the corpus analysis do this? Hyponyms?
    return result

#Note: excel data is not optimally formatted, so linear search is used
#      this may be changed to binary search later on when the files are in alphabetical order

def excel_data(word: str)->[str]:
    """returns a list of all excel data"""
    result = [[],[],[],[],[]]
    result[0] = tasa_data(word)
    result[1] = aoa_data(word)
    result[2] = awl_data(word)
    result[3] = subtlex_data(word)
    result[4] = zeno_data(word)
    return result    

def tasa_data(word: str)->int:
    """locates and returns a word's tasa data"""
    result = None
    for pos in range(tasa.nrows):
        if (word == tasa.cell(pos,0).value):
            result = tasa.cell(pos,1).value
            break
        pos += 1
    return result

def aoa_data(word: str)->[str]:
    """returns all available aoa data"""
    result = [None,None,None,None,None,None]
    for pos in range(aoa.nrows):
        if (word == aoa.cell(pos,0).value):
            result[0] = aoa.cell(pos,1).value   #OccurTotal
            result[1] = aoa.cell(pos,2).value   #OccuurNum
            result[2] = aoa.cell(pos,3).value   #Freq_pm
            result[3] = aoa.cell(pos,4).value   #Rating.Mean
            result[4] = aoa.cell(pos,5).value   #Rating.SD
            result[5] = aoa.cell(pos,6).value   #Dunno
            break
        pos += 1
    return result

def awl_data(word: str)->[int]:
    """returns all available awl data"""
    result = None
    for pos in range(awl.nrows):
        if (word == awl.cell(pos,0).value):
            result = awl.cell(pos,1).value   #AWL rating
            break
        pos += 1
    return result

def subtlex_data(word: str)->[str]:
    """returns all available subtlex data"""
    result = [None,None,None,None,None,None,None,None]
    for pos in range(subtlex.nrows):
        if (word == subtlex.cell(pos,0).value):
            result[0] = subtlex.cell(pos,1).value   #FREQcount
            result[1] = subtlex.cell(pos,2).value   #CScount
            result[2] = subtlex.cell(pos,3).value   #FREQlow
            result[3] = subtlex.cell(pos,4).value   #Cdlow
            result[4] = subtlex.cell(pos,5).value   #SUBTL_WF
            result[5] = subtlex.cell(pos,6).value   #Log_10(WF)
            result[6] = subtlex.cell(pos,7).value   #SUBTL_CD
            result[7] = subtlex.cell(pos,8).value   #Log_10(CD)
            break
        pos += 1
    return result

def zeno_data(word: str)->[str]:
    """returns all available zeno data"""
    result = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
    for pos in range(zeno.nrows):
        if (word == zeno.cell(pos,0).value):
            result[0] = zeno.cell(pos,1).value   #sfi
            result[1] = zeno.cell(pos,2).value   #d
            result[2] = zeno.cell(pos,3).value   #u
            result[3] = zeno.cell(pos,4).value   #f
            result[4] = zeno.cell(pos,5).value   #gr1
            result[5] = zeno.cell(pos,6).value   #gr2
            result[6] = zeno.cell(pos,7).value   #gr3
            result[7] = zeno.cell(pos,8).value   #gr4
            result[8] = zeno.cell(pos,9).value   #gr5
            result[9] = zeno.cell(pos,10).value   #gr6
            result[10] = zeno.cell(pos,11).value  #gr7
            result[11] = zeno.cell(pos,12).value  #gr8
            result[12] = zeno.cell(pos,13).value  #gr9
            result[13] = zeno.cell(pos,14).value  #gr10
            result[14] = zeno.cell(pos,15).value  #gr11
            result[15] = zeno.cell(pos,16).value  #gr12
            result[16] = zeno.cell(pos,17).value  #gr13
            break
        pos += 1
    return result











if __name__ == '__main__':
    run()
