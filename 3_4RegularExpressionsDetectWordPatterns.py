# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 15:31:36 2014
Natural Language Processing with Python
3.4 Regular Expresions for detecting Word Patterns

@author: Beto
"""
import nltk

#preprocess text to remove any proper names
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
#['a', 'aa', 'aal', 'aalii', 'aam', 'aardvark', 'aardwolf', 'aba', 'abac', 'abaca', 'abacate', 'abacay', 'abacinate', 'abacination', 'abaciscus', 'abacist', 'aback', 'abactinal', 'abactinally',...

#palabras terminadas en 'ed' $ indica al final de
print [w for w in wordlist if re.search('ed$', w)]
#['abaissed', 'abandoned', 'abased', 'abashed', 'abatised', 'abed', 'aborted', 'abridged', 'abscessed', 'absconded', 'absorbed', 'abstracted', 'abstricted', 'accelerated', 'accepted', 'accidented',...

#if we want to count de ocurrence we use len() or sum( 1 ...)
len([w for w in wordlist if re.search('ed$', w)])
#9148
sum(1 for w in wordlist if re.search('ed$', w))
#9148

# palabras con . wildcard que matcha cualquier unico caracter
# ^ que empiezde con el patron
# $ que termine con el patron
print [w for w in wordlist if re.search('^..j..t..$', w)]
#['abjectly', 'adjuster', 'dejected', 'dejectly', 'injector', 'majestic', 'objectee', 'objector', 'rejecter', 'rejector', 'unjilted', 'unjolted', 'unjustly']

#? previous character optional ^e-?mail$
print [w for w in wordlist if re.search('^e-?mail$', w)]

#RANGES AND CLOSURES
#textonimos
#  1       2 ABC     3 DEF
#  4 GHI   5 JKL     6 MNO
#  7 PQRS  8 TUV     9 WXYZ
# textonimos of key secuence 4653
print [w for w in wordlist if re.search('^[ghi][mno][jlk][def]$), w)]

print [w for w in wordlist if re.search('^[ghijklmno]+$', w)]
#print [w for w in wordlist if re.search('^[g-o]+$',w)]
#['g', 'ghoom', 'gig', 'giggling', 'gigolo', 'gilim', 'gill', 'gilling', 'gilo', 'gim', 'gin', 'ging', 'gingili', 'gink', 'ginkgo', 'ginning', 'gio', 'glink', 'glom', 'glonoin', 'gloom', 'glooming

# solo las teclas 4,5 6
print [ w for w in wordlist if re.search('^[a-fj-o]+$', w)]

#explore + symbol a bit further
# + * Kleene closures
chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
print [w for w in chat_words if re.search('^m+i+n+e+$', w)]
#['miiiiiiiiiiiiinnnnnnnnnnneeeeeeeeee', 'miiiiiinnnnnnnnnneeeeeeee', 'mine', 'mmmmmmmmiiiiiiiiinnnnnnnnneeeeeeee']

print [w for w in chat_words if re.search('^m*i*n*e*$', w)]
#['', 'e', 'i', 'in', 'm', 'me', 'meeeeeeeeeeeee', 'mi', 'miiiiiiiiiiiiinnnnnnnnnnneeeeeeeeee', 'miiiiiinnnnnnnnnneeeeeeee', 'min', 'mine', 'mm', 'mmm', 'mmmm', 'mmmmm', 'mmmmmm', 'mmmmmmmmiiiiiiiiinnnnnnnnneeeeeeee', 'mmmmmmmmmm', 'mmmmmmmmmmmmm', 'mmmmmmmmmmmmmm', 'n', 'ne']


print [w for w in chat_words if re.search('^[ha]+$', w)]
#['a', 'aaaaaaaaaaaaaaaaa', 'aaahhhh', 'ah', 'ahah', 'ahahah', 'ahh', 'ahhahahaha', 'ahhh', 'ahhhh', 'ahhhhhh', 'ahhhhhhhhhhhhhh', 'h', 'ha', 'haaa', 'hah', 'haha', 'hahaaa', 'hahah', 'hahaha', 'hahahaa', 'hahahah', 'hahahaha', 'hahahahaaa', 'hahahahahaha', 'hahahahahahaha', 'hahahahahahahahahahahahahahahaha', 'hahahhahah', 'hahhahahaha']

# [^aeiouAEIOU] matches any character other than a vowel

wsj = sorted(set(nltk.corpus.treebank.words())
print [w for w in wsj if re.search('^[^aeiouAEIOU]+$', w)]
#['!', '#', '$', '%', '&', "'", "''", "'30s", "'40s", "'50s", "'80s", "'82", "'86", "'S", "'d", "'ll", "'m",

print [w for w in wsj if re.search('[0-9]+\.[0-9]+$', w)]
#['0.0085', '0.05', '0.1', '0.16', '0.2', '0.25', '0.28', '0.3', '0.4', '0.5', '0.50', '0.54', '0.56', '0.60', '0.7', '0.82', '0.84', '0.9', '0.95', '0.99', '1.01', '1.1', '1.125', '1.14'

print [w for w in wsj if re.search('^[A-Z]+\$$', w)]
#['C$', 'US$']

print  [w for w in wsj if re.search('^[0-9]{4}$', w)]
#['1614', '1637', '1787', '1901', '1903', '1917', '1925', '1929', '1933', '1934', '1948', '1953', '1955', '1956', '1961',

print  [w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)]
#['10-day', '10-lap', '10-year', '100-share', '12-point', '12-year', '14-hour', '15-day', '150-point', '190-point',

print [w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)]
['black-and-white', 'bread-and-butter', 'father-in-law', 'machine-gun-toting', 'savings-and-loan']

print [w for w in wsj if re.search('(ed|ing)$', w)]
['62%-owned', 'Absorbed', 'According', 'Adopting', 'Advanced', 'Advancing', 'Alfred', 'Allied', 'Annualized', 'Anything', 'Arbitrage-related', 'Arbitraging', 'Asked', 'Assuming'

