# UI
# Author :      Nathan Krueger
# Created       5:00 PM 7/16/15
# Last Updated  2:55 PM 7/24/15
# Version       1.0

#import controller


#menu = """
#commands
#"""

#def main()->None:
    #"""Runs the user interface at a high level"""
    #return

def setup()->str:
    """Asks the user for a corpus refrence"""
    #print(nltk.book.texts())
    corpus = ""
    word = ""
    while True:
        corpus = input("Please enter an available corpus to refrence (ex text1): ")
        if corpus != "":
            #this is temporary
            if (corpus not in ['text1','text2','text3','text4','text5','text6','text7','text8','text9']):
                print("This corpus does not exist or is not available")
            else:
                break
    word = input("Please enter a word to analyze: ").lower()
    return (corpus, word)

#def interface()->None:
    #"""asks the user what to do and then asks the controller to do it"""
    #while True:
        #cmd = input(menu).strip().lower()
        #if cmd == ?:
        #if cmd == 'q':
            #print("Goodbye")
            #break
    #return

def return_data(data: [str])->None:
    """displays the data collected in the controller module"""
    #from nltk
    print("""
Total number of tokens:             {}
Number of unique tokens:            {}
Richness of the text:               {}
Count of word's occurences:         {}
Rate of word's occurence per token: {}
""".format(data[0][0],data[0][1],data[0][2],data[0][3], data[0][4]))
    
    #parts of speech and defintions from wordnet
    print("Defintions:")
    for def_index in range(len(data[1][0])):
          if data[1][1][def_index] == 'n':
              print("noun: {}".format(data[1][0][def_index]))
          if data[1][1][def_index] == 'a':
              print("adjective: {}".format(data[1][0][def_index]))
          if data[1][1][def_index] == 's':
              print("satellite adjective: {}".format(data[1][0][def_index]))
          if data[1][1][def_index] == 'r':
              print("adverb: {}".format(data[1][0][def_index]))
          if data[1][1][def_index] == 'v':
              print("verb: {}".format(data[1][0][def_index]))

    #related words by wordnet
    print("\nRelated words:")
    print("Synonyms:")
    for syn in data[1][2]:
        print(syn)
    print("\nAntonyms:")
    for ant in data[1][3]:
        print(ant)
    print("\nHypernyms:")
    for hyper in data[1][4]:
        print(hyper)
    print("\nHyponyms:")
    for hypo in data[1][5]:
        print(hypo)

    #Excel data
    print("\nTASA number: {}".format(data[2][0]))
    
    print("\nAOA data:")
    print("OccurTotal:      {}\nOccurNum:        {}\nFreq_pm:         {}\nRating.Mean:     {}\nRating.SD:       {}\n(unknown value): {}".format(
        data[2][1][0],data[2][1][1],data[2][1][2],data[2][1][3],data[2][1][4],data[2][1][5]))
    
    print("\nAWL value: {}".format(data[2][2]))
    
    print("\nSUBTLEX data:")
    print("""FREQcount:  {}\nCScount:    {}\nFREQlow:    {}\nCDlow:      {}\nSUBTL_WF:   {}\nLog_10(WF): {}
SUBTL_CD:   {}\nLog_10(CD): {}""".format(data[2][3][0],data[2][3][1],data[2][3][2],data[2][3][3],
                                       data[2][3][4],data[2][3][5],data[2][3][6],data[2][3][7]))
    
    print("\nZeno data:")
    print("""sfi:  {}\nd:    {}\nu:    {}\nf:    {}\ngr1:  {}\ngr2:  {}\ngr3:  {}\ngr4:  {}\ngr5:  {}\ngr6:  {}
gr7:  {}\ngr8:  {}\ngr9:  {}\ngr10: {}\ngr11: {}\ngr12: {}\ngr13: {}""".format(
    data[2][4][0],data[2][4][1],data[2][4][2],data[2][4][3],data[2][4][4],data[2][4][5],data[2][4][6],
    data[2][4][7],data[2][4][8],data[2][4][9],data[2][4][10],data[2][4][11],data[2][4][12],data[2][4][13],
    data[2][4][14],data[2][4][15],data[2][4][16]))
    
    return

#parts of speech conversion: ADJ, ADJECTIVE_SATELLITE, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'
#for synset in wn.synsets('mint', wn.NOUN):
#     print(synset.name() + ':', synset.definition())

if __name__ == '__main__':
    import nltk
    from nltk.book import *
    setup()
