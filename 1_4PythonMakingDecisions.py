# -*- coding: utf-8 -*-
"""
Created on Sat Nov 08 17:58:45 2014
1_4PythonMakingDecisionsTakingControl
@author: Beto
"""
from nltk.book import *

sent7
#['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the', 'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']

[w for w in sent7 if len(w) > 4]
#['Pierre', 'Vinken', 'years', 'board', 'nonexecutive', 'director']

[w for w in sent7 if len(w) < 4]
#[',', '61', 'old', ',', 'the', 'as', 'a', '29', '.']
[w for w in sent7 if len(w) <= 4]
#[',', '61', 'old', ',', 'will', 'join', 'the', 'as', 'a', 'Nov.', '29', '.']
[w for w in sent7 if len(w) == 4]
#['will', 'join', 'Nov.']
[w for w in sent7 if len(w) != 4]
#['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'the', 'board', 'as', 'a', 'nonexecutive', 'director', '29', '.']

#Some word comparison operators
s.startswith(t)         # Test if s start with t
s.endswith(t)           # Test if s ends with t
t in s                  # Test if t is contained inside s
s.islower()             # Test if all cased characters in s are lowercase
s.isupper()             # Test if all cased characters in s are uppercase
s.isalpha()             # Test if all characters in s are alphabetic
s.isdigit()             # Test if all character in s are digits
s.istitle()             # Test if s is titlecased (all words in s have initial capitals)

sorted([w for w in set(text1) if w.endswith('ableness')])
#['comfortableness', 'honourableness', 'immutableness', 'indispensableness', 'indomitableness', 'intolerableness', 'palpableness', 'reasonableness', 'uncomfortableness']

sorted([term for term in set(text4) if 'gnt' in term])
#['Sovereignty', 'sovereignties', 'sovereignty']

sorted([item for item in set(text6) if item.istitle()])
#['A', 'Aaaaaaaaah', 'Aaaaaaaah', 'Aaaaaah', 'Aaaah', 'Aaaaugh', 'Aaagh', 'Aaah', 'Aaauggh', 'Aaaugh', 'Aaauugh', 'Aagh', 'Aah', 'Aauuggghhh', 'Aauuugh', 'Aauuuuugh', 'Aauuuves', 'Action', 'Actually',

sorted([item for item in set(sent7) if item.isdigit()])
#['29', '61']

sorted([w for w in set(text7) if '-' in w and 'index' in w])
#['Stock-index', 'index-arbitrage', 'index-fund', 'index-options', 'index-related', 'stock-index']

sorted([wd for wd in set(text3) if wd.istitle() and len(wd) > 10])
#['Abelmizraim', 'Allonbachuth', 'Beerlahairoi', 'Canaanitish', 'Chedorlaomer', 'Girgashites', 'Hazarmaveth', 'Hazezontamar', 'Ishmeelites', 'Jegarsahadutha', 'Jehovahjireh', 'Kirjatharba', 'Melchizedek', 'Mesopotamia', 'Peradventure', 'Philistines', 'Zaphnathpaaneah']

sorted([w for w in set(sent7) if not w.islower()])
#[',', '.', '29', '61', 'Nov.', 'Pierre', 'Vinken']

sorted([ t for t in set(text2) if 'cie' in t or 'cei' in t])
#['ancient', 'ceiling', 'conceit', 'conceited', 'conceive', 'conscience', 'conscientious', 'conscientiously', 'deceitful', 'deceive',...

#Operating on Every Element
#[len(w) for w in text1]

#[w.upper() for w in text1]

#len(text1)
#len(set(text1))
#len(set([word.lower() for word in text1]))
#len(set([word.lower() for word in text1 if word.isalpha()]))

#Nested Code Blocks
word = 'cat'
if len(word) < 5:
    print 'word length is less than 5'
    
if len(word) >= 5:
    print 'word length is greather than or equal to 5'
    
for word in ['Call','me','Ismael','.']:
    print word
    
sent1 = ['Call','me','Ismael','.']
for elem in sent1:
    if elem.endswith('i'):
        print elem
        
tricky = sorted([w for w in set(text2) if 'cie' in w or 'cei' in w])
for word in tricky:
    print word,
    
