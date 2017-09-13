# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 18:30:44 2014

1_3SimpleStatistics
@author: Beto
"""

'''
>>> saying = ['After','all','is','said','and','done',
... 'more','is','said','than','done']
>>> tokens = set(saying)
>>> tokens
set(['and', 'all', 'said', 'is', 'After', 'done', 'than', 'more'])
>>> tokens = sorted(tokens)
>>> tokens
['After', 'all', 'and', 'done', 'is', 'more', 'said', 'than']
>>> tokens[-2:]
['said', 'than']

>>> text1
<Text: Moby Dick by Herman Melville 1851>
>>> fdist1 = FreqDist(text1)
>>> fdist1
<FreqDist with 19317 samples and 260819 outcomes>
>>>vocabulary1 = fdist1.keys()
>>> vocabulary1[:50]
[',', 'the', '.', 'of', 'and', 'a', 'to', ';', 'in', 'that', "'", '-', 'his', 'it', 'I', 's', 'is', 'he', 'with', 'was', 'as', '"', 'all', 'for', 'this', '!', 'at', 'by', 'but', 'not', '--', 'him', 'from', 'be', 'on', 'so', 'whale', 'one', 'you', 'had', 'have', 'there', 'But', 'or', 'were', 'now', 'which', '?', 'me', 'like']
>>> fdist1['whale']
906
>>> fdist1.plot(50, cumulative= True)
>>> fdist1.hapaxes()
>>> setText1 = set(text1)
>>> long_words = [ w for w in setText1 if len(w) > 15]
>>> sorted(long_words)
['CIRCUMNAVIGATION', 'Physiognomically', 'apprehensiveness', 'cannibalistically', 'characteristically', 'circumnavigating', 'circumnavigation', 'circumnavigations', 'comprehensiveness', 'hermaphroditical', 'indiscriminately', 'indispensableness', 'irresistibleness', 'physiognomically', 'preternaturalness', 'responsibilities', 'simultaneousness', 'subterraneousness', 'supernaturalness', 'superstitiousness', 'uncomfortableness', 'uncompromisedness', 'undiscriminating', 'uninterpenetratingly']
>>> 

>>> text5
<Text: Chat Corpus>
>>> fdist5 = FreqDist(text5)
>>> sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])
['#14-19teens', '#talkcity_adults', '((((((((((', '........', 'Question', 'actually', 'anything', 'computer', 'cute.-ass', 'everyone', 'football', 'innocent', 'listening', 'remember', 'seriously', 'something', 'together', 'tomorrow', 'watching']
>>> 

#Collocations and Bigrams
#collocations sequence of words that occur  together usually often

>>> bigrams(['Estos','son','bigramas','entendido'])
[('Estos', 'son'), ('son', 'bigramas'), ('bigramas', 'entendido')]

>>> text1.collocations()
Building collocations list
Sperm Whale; Moby Dick; White Whale; old man; Captain Ahab; sperm
whale; Right Whale; Captain Peleg; New Bedford; Cape Horn; cried Ahab;
years ago; lower jaw; never mind; Father Mapple; cried Stubb; chief
mate; white whale; ivory leg; one hand
>>> 

#Counting Other Things

[len(w) for w in text1]
#[1, 4, 4, 2, 6, 8, 4, 1, 9, 1, 1, 8, 2, 1, 4, 11, 5, 2, 1, 7, 6, 1, 3, 4, 5, 2, ...]

fdist = FreqDist([len(w) for w in text1])

fdist
#<FreqDist with 19 samples and 260819 outcomes>

fdisk.keys()
#[3, 1, 4, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20]

fdist.items()
#[(3, 50223), (1, 47933), (4, 42345), (2, 38513), (5, 26597), (6, 17111), (7, 14399), (8, 9966), (9, 6428), (10, 3528), (11, 1873), (12, 1053), (13, 567), (14, 177), (15, 70), (16, 22), (17, 12), (18, 1), (20, 1)]

fdist.max()
#50223

fdist.freq(3)
#0.19255882431878046

#Functions defined for NLTK´s frequency distributions
fdist = FreqDist(samples) #Create a frequency distribution containing the given samples
fdist.inc(sample)         #increment the count for this sample
fdist['moustrous']        #Count of the number of times a given sample occured
fdist.freq('monstrous')   #Frequency of a given sample
fdist.N()                 #Total number of samples
fdist.keys()              #The samples sorted in order of decreasing frequency
for sample in fdist:      #Iterate over the samples, in order of decreasing frequency
for sample in fdist:
   print sample
fdist.max()               #Sample with the greatest count
fdist.tabulate()          #tabulate the frequency distribution
fdist.plot()              #Graphical plot of the frequency distribution
fdist.plot(cumulative=True)  #Cumulative plot of the frequency distribution
fdist1 < fdist2           #Test if samples in fdist1 occur less frequently than in fdist2

