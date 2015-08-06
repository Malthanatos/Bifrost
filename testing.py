# Testing
# Author :      Nathan Krueger
# Created       4:30 PM 7/16/15
# Last Updated  3:30 PM 7/23/15
# Version       0.5

import nltk
import xlrd
import xlwt
#from nltk.book import *
from nltk.corpus import wordnet

sheet = ''

def run():
    #texts() or sents() for material list
    #text1 -> name of text
    global sheet
    
    workbook = xlrd.open_workbook('tasa.xlsx')
    sheet = workbook.sheet_by_index(0)
    run2()
    return

def run2():
    for value in sheet.col_values(0):
        if value[0] == 'd':
            print(value)
    '''word = 'whale'
    result = [[],[],[],set(),[]]
    word_info = wordnet.synsets(word)[0]
    lemmas = wordnet.lemmas(word)
    for lemma in lemmas:
        print(lemma.hypernyms())
        print(lemma.hyponyms())
        print(lemma.pertainyms())
        #print(lemma.synonyms())
        print(lemma.antonyms())'''
    '''for synset in wordnet.synsets(word):
        result[0].append(synset.definition())
        result[1].append(synset.pos())
    result[2] = word_info.lemma_names()
    #result[3] = [lemma.antonyms() for lemma in lemmas]
    for lemma in lemmas:
        for word in lemma.antonyms():
            result[3].add(word.name())
    #result[4] = word_info.lemma_names()
    print(result)'''
    
    return

'''
def excel():
    #reading
        workbook = xlrd.open_workbook('simple.xls')
        #if that does not work try unicode (above is ASCII)
            #workbook = xlrd.open_workbook('my_file_name.xls', encoding='cp1252')
        #for large files this only accesses the current "sheet"
            #workbook = xlrd.open_workbook('my_file_name.xls', on_demand = True)
        worksheet = workbook.sheet_by_index(0)
            #worksheet = workbook.sheet_by_name('???')
            #number_of_sheets = workbook.nsheets
            #list_of_sheet_names = workbook.sheet_names()
        v = worksheet.cell(0,0).value
            #you can iterate using the x or y coordinates
            #to detect empty cells
            worksheet.cell(0,0).value == xlrd.empty_cell_value
        #return list of all cells in a column/row (swap col/row)
        worksheet.col(0)
        #return list of all values in a column/row
        worksheet.col_values(0, start = 0, end = None)
            #return a selection of column/row cells
            #worksheet.col_slice(0, start_rowx = 0, end_rowx = None)
        #return number of rows/columns
        worksheet.nrows
        worksheet.ncols
    #writing
        workbook = xlwt.Workbook()
        workbook.save('file_name.xls')
        sheet = workbook.add_sheet('sheet_name')
        sheet.write(0,0, 'data')
        row = sheet.row(1)
        row.write(0, 'data')
        #delete all row data
            row.flush_row_data()
        #set width of a column in pixels
            sheet.col(0).width = 625
        #styles can also be done, but are not written here
    return

def ntlk():
    nltk (ch 1 and 2)
    list occurences of a word centered in a definitly sized block of text
    text1.concordance("monstrous")
    words that are often near the given word
    text1.similar("monstrous")
    lists common contexts for a given set of words if any
    text1.common_contexts(['word1', 'word2'])
    graph dispersion of given words accorss the text's length (requires secondary packages)
    text1.dispersion_plot(['word1', 'word2', 'word3'...])
    number of words, punctuation; aka tokens
    len(text3)
    list of tokens
    len(set(text3))
    ration of unqiue tokens over all words
    len(set(text3))/len(text3)
    count all occurences of a token
    text1.count('word')
    give a statistic on a basic frequency distribution
    FreqDist(text1)
    give a list of tuples for most frequent x tokens
    FreqDist(text1).most_common(x)
    recall you can use max on tuples to find most common or largest ???
    see website for further operations
    a list of tuple couples that show words that appear next to each other
    bigrams(list of words)
    words that usually appear next to each other in a text
    text1.collocations()
    list available files
    nltk.corpus.abc.fileids()
    list types of literature in the given selection
    brown.categories()

word net (ch 2, section 5)
    return a synset object; definition, type (noun/verb/etc), and number of possible meanings
    wn.synsets('murmured')
    list the possible synonyms based on current knowledge
    wn.synset('murmur.v.01').lemma_names()
    * actually, as a first level project I would like to know how many
    * synsets are associated with each lemma, and what the relationship between
    * lemma frequency and number of connected sysets is. 
    return textual definition of the word/synset
    wn.synset('murmur.v.02').definition()
    return a list of example sentences
    wn.synset('murmur.v.02').examples()
    return list of synonymous words/lemmas that can be further accessed for intormation
    wn.lemmas('word')
    return list of words that can be defined as being a sub-set of the word
    wn.synsets('motorcar.v.01').hyponyms() -> ambulence, SUV, wagon, etc
    degree of generality of a word
    wn.synset('baleen_whale.n.01').min_depth()
    ex. entity = 0, baleen_whale = 14 (14 levels from specificity to generality)
    return

    from nltk.corpus import wordnet as wn
>>> dog = wn.synset('dog.n.01')
>>> hyp = lambda s:s.hypernyms()
>>> from pprint import pprint
>>> pprint(dog.tree(hyp))
    -> tree of words of decreasing specificity
'''

if __name__ == "__main__":
    run()
