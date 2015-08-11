# UI
# Author :      Nathan Krueger
# Created       5:00 PM 7/16/15
# Last Updated  2:00 PM 8/11/15
# Version       1.7

#import controller
#controller.excel_setup()
import excel
import xlrd, xlwt
from os.path import exists

corpora = []
max_index = 0
output = 0
sort_type = 0

menu = """
Enter a command:
output   change type of output between shell text and external documentation
sort     sort the output based on a particular value
newc     add a new corpus (not working right now)
listc    lists all available corpora by registered name
swa      single word analysis
swac     single word analysis with a corpus
mwa      multi-word analysis
mwac     multi-word analysis with a corpus
mwaxl    multi-word analysis using input from an excel spreadsheet
polys    polysemy rating for a selection of words
mindep   mindepth of a selection of words
dtree    depth tree of a given word (working on making it neater)

q        quit

command: """

def setup()->None:
    '''sets up the user interface'''
    global corpora, max_index
    corpora = open('corpora.txt').read().splitlines()
    max_index = len(corpora)
    return

def interface()->(str, int):
    """asks the user what to do and then asks the controller to do it"""
    global output, sort_type
    while True:
        cmd = input(menu).strip().lower()
        if cmd == 'output':
            output = change_output()
            return (None,None)
        elif cmd == 'sort':
            sort_type = sort_change()
            return (None,None)
        elif cmd == 'newc':
            return ('newc', newc())
        elif cmd == 'listc':
            print('Available corpora:')
            for c in corpora:
                print(c)
            return (None,None)
        elif cmd == 'swa':
            return ('swa', swa())
        elif cmd == 'swac':
            return ('swac', swac())
        elif cmd == 'mwa':
            return ('mwa', mwa())
        elif cmd == 'mwac':
            return ('mwac', mwac())
        elif cmd == 'mwaxl':
            return ('mwaxl', mwaxl())
        elif cmd == 'polys':
            return ('polys', polys())
        elif cmd == 'mindep':
            return ('mindep', mindep())
        elif cmd == 'dtree':
            return ('dtree', dtree())
        elif cmd == 'q':
            print("Goodbye")
            return ('quit', None)
        else:
            print("Invalid command, please try again")
    return

def change_output()->int:
    '''allows user to change the programs output to text and/or excel file'''
    while True:
        output_type = input("Change output to (excel, shell text (default), both): ").strip().lower()
        if output_type in ['text', 'shell text', 'default']:
            return 0
        elif output_type == 'excel':
            return 1
        elif output_type == 'both':
            return 2
        else:
            print("Invalid output type, please select from: excel, text, or both")

def sort_change()->str:
    '''changes how the outputs are ordered'''
    print("The words will be printed in order followed by their analysis")
    possibles = ['default','def_count',]#'TASA','AWL','sfi (from Zeno)','d (from Zeno)']
    print("Possible sort methods: {}".format(possibles))
    while True:
        result = input("Please enter the basis for output sorting: ").strip().lower()
        if result not in possibles:
            print("This sort method is not valid")
        break
    if result == 'default':
        return 0
    elif result == 'def_count':
        return 1

def newc()->('file', str):
    """tell controller to add a new corpus given its name"""
    print("""Please enter the fileid of the new corpus exactly as it is
(including the extension; only .txt is currently supported) and that the
file is present in the current directory:
""")
    while True:
        file_name = input("fileid of new corpus: ")
        try:
            if file_name.split('.')[1] != 'txt':
                print("This file format is not currently supported")
                continue
            assert exists(file_name)
            #file = open(file_name, 'r')
            #file.close()
        except:
            print("This corpus is not available, please make sure that you typed it correctly")
            return newc()
        name = input("Please enter the name of the corpus: ")
        break
    return (file_name, name)

def swa()->str:
    """run an analysis on a signle word"""
    word = input("Please enter a word to analyze: ").strip().lower()
    return word

def swac()->(int,str):
    """run an analysis on a signle word based on a corpus"""
    while True:
        corpus = input("Please enter an available corpus to refrence by index number: ")
        try:
            corpus = int(corpus)
            if corpus > max_index or corpus < 1:
                print("This corpus does not exist or is not available")
            else:
                break
        except:
            print("This is not a valid corpus index (valid indicies are 1-{})".format(max_index))
    word = input("Please enter a word to analyze: ").strip().lower()
    return (corpus, word)

def mwa()->[str]:
    """run an analysis on several words"""
    words = input("Please enter a series of words to analyze seperated only by spaces: ").strip().lower().split()
    return words

def mwac()->(str,[str]):
    """run an analysis on several words based on a corpus"""
    while True:
        corpus = input("Please enter an available corpus to refrence by index number: ")
        try:
            corpus = int(corpus)
            if corpus > max_index or corpus < 1:
                print("This corpus does not exist or is not available")
            else:
                break
        except:
            print("This is not a valid corpus index (valid indicies are 1-{})".format(max_index))
    words = input("Please enter a series of words to analyze seperated only by one or more spaces: ").strip().lower().split()
    return (corpus, words)

def mwaxl()->(str, int):
    """run an analysis on many words from an excel file"""
    #global file, sheet
    print("""Please enter the fileid of the excel file exactly as it is
(including the extension), please ensure that the file is present in
the current folder and that all words are listed in the first column
""")
    while True:
        file = input("fileid of excel document: ").strip()
        sheet = input("Please enter the sheet number to check: ")
        try:
            sheet = int(sheet)
        except:
            print("Sheet number is not valid")
            continue
        if sheet < 0:
            print("Sheet number cannot be negative")
            continue
        try:
            file = xlrd.open_workbook(str(file))
            sheet = file.sheet_by_index(int(sheet))
            break
        except:
            print("This excel document or sheet is not available, please make sure that you \ntyped it correctly")
            continue
    return (file, sheet)

def polys()->str:
    '''returns a list of polysemy ratings for a given wordset'''
    while True:
        print("Word sources: default, manual (currently the only options available)")
        word_source = input("Please enter a source for the words to analyze: ").strip().lower()
        #result = controller.polysemy(word_source)
        if word_source in ['default', 'manual']:
            return word_source
        else:
            print("Invalid word source")

def mindep()->str:
    '''returns the min depth of all of the given words'''
    while True:
        print("Word sources: default, manual (currently the only options available)")
        word_source = input("Please enter a source for the words to analyze: ").strip().lower()
        #result = controller.polysemy(word_source)
        if word_source in ['default', 'manual']:
            return word_source
        else:
            print("Invalid word source")

def dtree()->str:
    '''returns the depth tree for a given word'''
    return input("Please enter a word to analyze: ").strip().lower()

def output_data(value)->None:
    '''selects between output styles and call the correct function/s'''
    value = (sort(value[0]), value[1])
    if output != 1:
        print_data(value)
    if output != 0:
        data_to_file(value)

def data_to_file(value)->None:
    '''outputs the data as a file of specified name and type'''
    print("""
Warning: for the moment this program cannot append to files,
only create and overwrite them, please be careful about using existing files
You can specify a different sheet number to use if you wish to add to a file

Also, please choose a file type of either .xls or .xlsx (old vs. new excel)
          """)
    while True:
        file_name = input("Please enter the name of the file you would to craete, including the extension: ")
        print("\n{}\n".format(file_name))
        sure = input("Are you sure this is the file name you wish to use (y/n)").strip().lower()
        if sure not in ['y', 'yes']:
            continue
        if file_name.split('.')[1] not in ['xls','xlsx']:
            print("This file type is not currently supported")
            continue
        while True:
            sheet_index = input("Please enter a sheet number: ").strip().lower()
            try:
                sheet_index = int(sheet_index)
                break
            except:
                print("Invalid sheet number")
        break
    file_from_data(value, file_name, sheet_index)
    return

def file_from_data(value, file_name: str, sheet_index: int)->None:
    '''creates an output file using the given name'''
    data, function = value
    if function in ['newc','polys','mindep','dtree']:
        return
    excel.file_setup(data, file_name, sheet_index)
    return

def print_data(value)->None:
    """prints the data"""
    #can probably shorten this if I try
    data, function = value
    if function == 'newc':
        if data:
            print("New corpus has been sucesfully installed")
        else:
            print("New corpus could not be installed...")
    elif function in ['swa', 'swac']:
        print("\nWord: {}".format(data[0][0]))
        if function == 'swac':
            print_nltk(data[0][1])
        print_wordnet(data[0][2])
        print_excel(data[0][3])
    elif function in ['mwa', 'mwac', 'mwaxl']:
        for word in data:
            print("\n{}\nWord: {}".format('*'*80,word[0]))
            if function == 'mwac':
                print_nltk(word[1])
            print_wordnet(word[2])
            print_excel(word[3])
    elif function == 'polys':
        print("Number of part of speech definitons for each word:")
        print("\nWord                Noun  Adj  SatAdj  Adv  Verb")
        for word in data:
            print("{:18}{:6}{:5}{:8}{:5}{:6}".format(word[0],word[1],word[2],word[3],word[4],word[5]))
    elif function == 'mindep':
        print("Min depth of the most common definition for each word:")
        print("\nWord           Min depth")
        for word in data:
            print("{:18}{:6}".format(word[0],word[1]))
    elif function == 'dtree':
        print("Multiple entires on the same line are equivalent")
        from pprint import pprint
        pprint(data)
    return

def print_nltk(data)->None:
    '''prints data from corpus'''
    print("""
Total number of tokens:             {}
Number of unique tokens:            {}
Richness of the text:               {}
Count of word's occurences:         {}
Rate of word's occurence per token: {}
""".format(data[0],data[1],data[2],data[3], data[4]))
    return

def print_wordnet(data)->None:
    '''prints data from wordnet'''
    #parts of speech and defintions
    print("Defintions:")
    for def_index in range(len(data[0])):
          if data[1][def_index] == 'n':
              print("noun: {}".format(data[0][def_index]))
          if data[1][def_index] == 'a':
              print("adjective: {}".format(data[0][def_index]))
          if data[1][def_index] == 's':
              print("satellite adjective: {}".format(data[0][def_index]))
          if data[1][def_index] == 'r':
              print("adverb: {}".format(data[0][def_index]))
          if data[1][def_index] == 'v':
              print("verb: {}".format(data[0][def_index]))
    #related words
    print("\nRelated words:")
    print("Synonyms:")
    for syn in data[2]:
        print(syn)
    print("\nAntonyms:")
    for ant in data[3]:
        print(ant)
    print("\nHypernyms:")
    for hyper in data[4]:
        print(hyper)
    print("\nHyponyms:")
    for hypo in data[5]:
        print(hypo)
    return

def print_excel(data)->None:
    '''prints data from excel spreadsheets'''
    print("\nTASA number: {}".format(data[2]))
    
    print("\nAOA data:")
    print("OccurTotal:      {}\nOccurNum:        {}\nFreq_pm:         {}\nRating.Mean:     {}\nRating.SD:       {}\n(unknown value): {}".format(
        data[1][0],data[1][1],data[1][2],data[1][3],data[1][4],data[1][5]))
    
    print("\nAWL value: {}".format(data[0]))
    
    print("\nSUBTLEX data:")
    print("""FREQcount:  {}\nCScount:    {}\nFREQlow:    {}\nCDlow:      {}\nSUBTL_WF:   {}\nLog_10(WF): {}
SUBTL_CD:   {}\nLog_10(CD): {}""".format(data[3][0],data[3][1],data[3][2],data[3][3],
                                       data[3][4],data[3][5],data[3][6],data[3][7]))
    
    print("\nZeno data:")
    print("""sfi:  {}\nd:    {}\nu:    {}\nf:    {}\ngr1:  {}\ngr2:  {}\ngr3:  {}\ngr4:  {}\ngr5:  {}\ngr6:  {}
gr7:  {}\ngr8:  {}\ngr9:  {}\ngr10: {}\ngr11: {}\ngr12: {}\ngr13: {}""".format(
    data[4][0],data[4][1],data[4][2],data[4][3],data[4][4],data[4][5],data[4][6],
    data[4][7],data[4][8],data[4][9],data[4][10],data[4][11],data[4][12],data[4][13],
    data[4][14],data[4][15],data[4][16]))
    return

def sort(data)->list:
    '''uses the current sort method to sort the data'''
    if sort_type == 0:
        return data
    if sort_type == 1:
        data.sort(key = lambda x: len(x[2][0]), reverse = True)

    return data

#parts of speech conversion: ADJ, ADJECTIVE_SATELLITE, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'
#for synset in wn.synsets('mint', wn.NOUN):
#     print(synset.name() + ':', synset.definition())


#if __name__ == '__main__':
    #interface()
