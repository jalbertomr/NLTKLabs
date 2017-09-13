# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 18:43:16 2014
1_1 Natural Language Processing
@author: Beto
"""

from nltk.book import *
'''
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> 
'''
text1
#<Text: Moby Dick by Herman Melville 1851>
text2
#<Text: Sense and Sensibility by Jane Austen 1811>

text1.concordance('monster') 
'''
Building index...
Displaying 25 of 49 matches:
des cometh within the chaos of this monster ' s mouth , be it beast , boat , or
nter into the dreadful gulf of this monster ' s ( whale ' s ) mouth , are immed
time with a lance ; but the furious monster at length rushed on the boat ; hims
 . Such a portentous and mysterious monster roused all my curiosity . Then the 
and flank with the most exasperated monster . Long usage had , for this Stubb ,
ACK ).-- Under this head I reckon a monster which , by the various names of Fin
arned the history of that murderous monster against whom I and all the others h
ocity , cunning , and malice in the monster attacked ; therefore it was , that 
iathan is restricted to the ignoble monster primitively pursued in the North ; 
 and incontestable character of the monster to strike the imagination with unwo
mberment . Then , in darting at the monster , knife in hand , he had but given 
e rock ; instead of this we saw the monster sailing off with the utmost gravity
e at Constantinople , a great sea - monster was captured in the neighboring Pro
 Of what precise species this sea - monster was , is not mentioned . But as he 
man reasoning , Procopius ' s sea - monster , that for half a century stove the
hale ," as he called the fictitious monster which he declared to be incessantly
d his intention to hunt that mortal monster in person . But such a supposition 
ng us on and on , in order that the monster might turn round upon us , and rend
d famous , and most deadly immortal monster , Don ;-- but that would be too lon
oluntarily lifted his voice for the monster , though for some little time past 
s rescuing Andromeda from the sea - monster or whale . Where did Guido get the 
 huge corpulence of that Hogarthian monster undulates on the surface , scarcely
nd is drawn just balancing upon the monster ' s spine ; and standing in that pr
 of cutting - in ) hove over to the monster as if to a quay ; and a boat , hurr
eet in length . They fancy that the monster to which these arms belonged ordina
>>> 
'''
text1.similar('monster')
'''
Building word-context index...
whale ship sea world boat pequod whales other sun air cabin captain
crew head king leviathan thing water bed body
>>> 
'''
text2.common_contexts(['monstrous','very'])

text4.dispersion_plot(["citizen","democrazy","freedom","duties","America"])

text1.generate()

len(text3)

sorted(set(text3))

# make sure python uses foating point division
#from __future__ import division
len(text3)/len(set(text3))
#16.050197203298673

text3.count('smote')
#5

set(text1)
#set(['funereal', 'unscientific', 'divinely', 'foul', 'four', 'gag', 'prefix', 'woods', 'clotted', 'Duck', 'hanging',...

len(set(text1))
#19317

100 * text1.count('whale') / len(set(text1))
#4.690169280944246

100 * text1.count('car') / len(set(text1))
#0.005176787285810426

text1.concordance('car')
#Displaying 1 of 1 matches:
#ys to be at the expense of a separate car , specially reserved for the accommod

text1.concordance('beach')
#Displaying 18 of 18 matches:
#ney in a pedestrian trip to Rockaway Beach ? Why is almost every robust healthy
#re hillock , and elbow of sand ; all beach , without a background . There is mo
# that these Nantucketers , born on a beach , should take to the sea for a livel

100 * text1.count('beach') / len(set(text1))
#0.08282859657296682

def lexical_diversity(text):
    return len(text)/len(set(text))
    
def percentage(count, total):
    return 100 * count / total
    
lexical_diversity(text1)

lexical_diversity(text3)

percentage(4,5)
#80

percentage(text4.count('a'), len(text4))

sent = ['word1', 'word2', 'word3', 'word4', 'word5',
        'word6', 'word7', 'word8', 'word9', 'word10']

'''
>>> sent[0]
'word1'
>>> sent[1]
'word2'
>>> sent[9]
'word10'
>>> sent.index('word7')
6        
>>> sent[4:6]
['word5', 'word6']
>>> sent[4:7]
['word5', 'word6', 'word7']
>>> sent[4:0]
[]
>>> sent[4:1]
[]
>>> sent[4:2]
[]
>>> sent[4:3]
[]
>>> sent[4:4]
[]
>>> sent[4:5]
['word5']
>>> sent[4:6]
['word5', 'word6']
>>> sent[4:9]
['word5', 'word6', 'word7', 'word8', 'word9']
>>> 
>>> sent[0]='first'
>>> sent[9]='last'
>>> len(sent)
10
>>> sent[1:5]
['word2', 'word3', 'word4', 'word5']
>>> sent[1:9]
['word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9']
>>> sent[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> sent[0]='First'
>>> sent[9]='Last'
>>> sent
['First', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'Last']
>>> sent[3:5]=['tres','cinco']
>>> sent
['First', 'word2', 'word3', 'tres', 'cinco', 'word6', 'word7', 'word8', 'word9', 'Last']
>>> sent[3:8]=['tres','ocho']
>>> sent
['First', 'word2', 'word3', 'tres', 'ocho', 'word9', 'Last']
>>> 
>>> my_sent=['Bravely','bold','Sir','Robin',',','rode']
>>> my_sent.append(['forth','from','Camelot','.'])
>>> my_sent
['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode', ['forth', 'from', 'Camelot', '.']]
>>> my_sent=my_sent[1:6]
>>> my_sent
['bold', 'Sir', 'Robin', ',', 'rode']
>>> my_sent=['Bravely','bold','Sir','Robin',',','rode']
>>> my_sent.append('forth','from','Camelot','.')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (4 given)
>>> 
>>> my_sent
['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode']
>>> my_sent = my_sent + ['forth','from','Camelot','.']
>>> my_sent
['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode', 'forth', 'from', 'Camelot', '.']
>>> 
>>> noun_phrase = my_sent[1:4]
>>> noun_phrase
['bold', 'Sir', 'Robin']
>>> wOrDs = sorted(noun_phrase)
>>> wOrDs
['Robin', 'Sir', 'bold']
>>> 
>>> name = 'Monty'
>>> name[0]
'M'
>>> name[:4]
'Mont'
>>> 
>>> name * 2
'MontyMonty'
>>> name * 3
'MontyMontyMonty'
>>> name + '!'
'Monty!'
>>> 
>>> ' '.join(['Monty','Python'])
'Monty Python'
>>> 'Monty Python'.split()
['Monty', 'Python']