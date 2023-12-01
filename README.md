# Bifrost


Requires:

Python 3.3+, Natural Language Toolkit for Python (NLTK), XLRD and openpyxl for Python (reads and writes Excel files)

Recommended for full functionality: Numpy for Python, Matplotlib for Python

Use:

Download the repo and install the recommended Python packages using PIP or an alternate installer

Run Python in a shell and import run.py

Bifrost will provide instructions and a list of commands on startup

Running a selected command will provide the user with instructions specific to that command and will execute when given valid input/s

A second branch is available that only includes the polysemy and mindepth related functions

Bifrost commands:

output - change type of output between shell text and external documentation

sort - sort the output based on a particular value

newc - add a new corpus

listc - lists all available corpora by registered name

swa - single word analysis

swac - single word analysis with a corpus

mwaw - multi-word analysis using word definitions and POS

mwax - multi-word analysis using excel and wordnet data

mwac - multi-word analysis with a corpus

dwsa - dual-word similarity analysis

polys - polysemy rating for a selection of words

mindep - mindepth of word/s (first result only, see dtree for alternate synsets)

pol_min - runs both polysemy and mindepth analysis of a selection of words

dtree - depth tree of a given word (working on making it neater)

xhyper - returns the highest order x (given number) hypernyms of a word or words

q - quit


Additional Independent Functions:

BSSA (binary synset similarity analysis): given a set of word pairs, compare the similarity of each pair using a set of metrics provided by WordNet.

Use:

Import BSSA.py in a Python shell to run. Instructions are printed at runtime.

BSSA Instructions:

Enter the file you would like to analyze, acceptable file types are '.txt' and
'.xlsx'. The program will assume white-space based formatting for text files
and 2 words, separated by column, per row for excel files. Once the words have
been read into the program it will list them as pairs. If the pairs are
incorrect you can reformat the input document and start over. If they are
correct you can wait until the word definitions are compiled into a list and
then for every word you entered the program will automatically display the
known definitions for each word. If the word has no definitions it will be
replaced by "None" and that pair will be skipped. If the word has exactly one
definition it will be entered automatically. If there are multiple definitions
you will be asked to pick one. After a definition has been chosen it will be
printed back to you and the next word will be displayed. When all word
definitions are chosen the program will display the final synsets and ask you to
provide a name for a file to output the results to. The results are formatted
such that each word pair is listed followed by the three similarity comparisons
followed by the definitions used for the given words. Note that entering two
word definitions with different parts of speech will fail.

Please cite as:

Krueger, N., & Lawrence, J., (2016). Bifrost: Bridging linguistic, cognitive and computer science resources (VersionMaster). Retrieved from https://github.com/Malthanatos/Bifrost

We extracted a total of 174,487 definitions. We tabulated these unique senses and meanings to establish two measures: in part of speech senses and meanings (IPOSSAM) and the across part of speech senses and meanings (APOSSAM). For example, the word phone has two entries, one with the part of speech of noun and the other with the part of speech of verb. Phone has three noun definitions and only one verb definition. The APOSSAM value for phone on both entries is 4 (3 + 1), and the IPOSSAM value for phone as a noun is 3 and as a verb is 1. We recoded two WordNet part-of-speech labels (adjective and satellite adjective) as adjectives. 

WordNet Release 3.0. This software and database is being provided to you, the LICENSEE, by Princeton University under the following license. By obtaining, using, and/or copying this software and database, you agree that you have read, understood, and will comply with these terms and conditions: Permission to use, copy, modify, and distribute this software and database and its documentation for any purpose and without fee or royalty is hereby granted, provided that you agree to comply with the following copyright notice and statements, including the disclaimer, and that the same appear on ALL copies of the software, database, and documentation, including modifications that you make for internal use or for distribution. WordNet 3.0 Copyright 2006 by Princeton University. All rights reserved. THIS SOFTWARE AND DATABASE IS PROVIDED “AS IS” AND PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES OF MERCHANT- ABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE LICENSED SOFTWARE, DATABASE, OR DOCUMENTATION WILL NOT INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS, OR OTHER RIGHTS. The name of Princeton University or Princeton may not be used in advertising or publicity pertaining to distribution of the software and/or database. Title to copyright in this software, database, and any associated documentation shall at all times remain with Princeton University and LICENSEE agrees to preserve same.
