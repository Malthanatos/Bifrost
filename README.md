# Bifrost

Please cite as:
Lawrence, J., & Krueger, N. (2016). Bifrost: Bridging linguistic, cognitive and computer science resources (VersionMaster). Retrieved from https://github.com/Malthanatos/Bifrost

This program was developed with support from the University of California Academic Senate Council on Research, Computing, and Libraries (CORCL).

Please contract Joshua Lawrence at jflawren@uci.edu for any of the following papers that have used from data derived from the Bifrost program:

Lawrence, J. F., Hwang, J. K., Hagen, A., & Lin, G. (n.d.). What makes an academic word difficult to know?: Exploring lexical dimensions across novel measures of word knowledge. 

Lawrence, J.F., Hagen, A., Hwang, J. K., Lin, G., & Arne, L. (n.d.). Academic vocabulary and reading comprehension: Exploring the relationships across measures of vocabulary knowledge.

Lawrence, J. F., Lin, G., Jaeggi, S., Krueger, N., Hwang, J. K., & Hagen, A. (n.d.). Polysemy and semantic precision: Standardized semantic measures extracted from Wordnet for 100,000 words in English.

Lawrence, J. F., (n.d.) Semantic precision and polysemy: Key indices of word difficulty and utility for reading.

Word Analysis

Takes a given word and corpus and returns a series of formatted data points from available databases and functions.

Requires:
Python 3.3+, Natural Language Toolkit for Python (NLTK), XLRD, and openpyxl for Python (reads and writes Excel files)

Recommended for full functionality: Numpy for Python, Matplotlib for Python

Additonal Independent Functions:

BSSA (binary synset similarity analysis): given a set of word pairs, compare the similarity of each pair using a set of metrics provided by WordNet.