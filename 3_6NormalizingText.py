# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 17:02:50 2014
3_6NormalizingText
A further step is to make sure that the resulting form is a known word in a
dictionary, a task known as lemmatization
@author: Beto
"""

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government. Supreme executive power derives from
a mandete from the masses, not from some farcical aquatic ceremony."""
import nltk

tokens = nltk.word_tokenize(raw)
#>>>tokens
#['DENNIS', ':', 'Listen', ',', 'strange', 'women', 'lying', 'in', 'ponds', 'distributing', 'swords', 'is', 'no', 'basis', 'for', 'a', 'system', 'of', 'government.', 'Supreme', 'executive', 'power', 'derives', 'from', 'a', 'mandete', 'from', 'the', 'masses', ',', 'not', 'from', 'some', 'farcical', 'aquatic', 'ceremony', '.']

#Stemmers
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

[porter.stem(t) for t in tokens]
#['DENNI', ':', 'Listen', ',', 'strang', 'women', 'lie', 'in', 'pond', 'distribut', 'sword', 'is', 'no', 'basi', 'for', 'a', 'system', 'of', 'government.', 'Suprem', 'execut', 'power', 'deriv', 'from', 'a', 'mandet', 'from', 'the', 'mass', ',', 'not', 'from', 'some', 'farcic', 'aquat', 'ceremoni', '.']

[lancaster.stem(t) for t in tokens]
#['den', ':', 'list', ',', 'strange', 'wom', 'lying', 'in', 'pond', 'distribut', 'sword', 'is', 'no', 'bas', 'for', 'a', 'system', 'of', 'government.', 'suprem', 'execut', 'pow', 'der', 'from', 'a', 'mandet', 'from', 'the', 'mass', ',', 'not', 'from', 'som', 'farc', 'aqu', 'ceremony', '.']

#Example 3-1 Indexing a text using a stemmer
class IndexedText(object):
    
    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                for (i, word) in enumerate(text))
                                    
    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = width/4    #words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[-wc:i])
            rcontext = ' '.join(self._text[i:i + wc])
            ldisplay = '%*s' % (width, lcontext[-width:])
            rdisplay = '%-*s' % (width, rcontext[:width])
            print ldisplay, rdisplay
            
    def _stem(self, word):
        return self._stemmer.stem(word).lower()

porter = nltk.PorterStemmer()
grail = nltk.corpus.webtext.words('grail.txt')
text = IndexedText(porter, grail)
text.concordance('dog')
# dogs ! Go and boil your bottom , sons of
text.concordance('lie')
#lying in ponds distributing swords is no
#lies ! MINSTREL : [ singing ] Bravest of
#lie here . Oh , but you are wounded !   
#Lie down . [ clap clap ] PIGLET : Well  
#lies the Gorge of Eternal Peril , which

#Lemmatization
#The WordNet lemmatizer removes affixes only if the resulting word
#is in its dictionary

wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for  t in tokens]
#['DENNIS', ':', 'Listen', ',', 'strange', 'woman', 'lying', 'in', 'pond', 'distributing', 'sword', 'is', 'no', 'basis', 'for', 'a', 'system', 'of', 'government.', 'Supreme', 'executive', 'power', 'derives', 'from', 'a', 'mandete', 'from', 'the', 'mass', ',', 'not', 'from', 'some', 'farcical', 'aquatic', 'ceremony', '.']

#Generator Expression
#>>> text = '''"When I use a word," Humpty Dumpty said in rather a scornful tone,... "it means just what I choose it to mean -  neither more nor less."'''

#>>> type(text)
#<type 'str'>

#>>>type([w.lower() for w in nltk.word_tokenize(text)])
#<type 'list'>

#>>> type(w.lower() for w in nltk.word_tokenize(text))
#<type 'generator'>

'''
import profile

>>> profile.run("""type([w.lower() for w in nltk.word_tokenize(text)])""")
         540 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       39    0.000    0.000    0.000    0.000 :0(get)
      141    0.001    0.000    0.001    0.000 :0(group)
       71    0.000    0.000    0.000    0.000 :0(join)
       35    0.000    0.000    0.000    0.000 :0(lower)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(split)
        1    0.000    0.000    0.000    0.000 :0(strip)
       27    0.001    0.000    0.005    0.000 :0(sub)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.006    0.006 __init__.py:80(word_tokenize)
        0    0.000             0.000          profile:0(profiler)
        1    0.000    0.000    0.006    0.006 profile:0(type([w.lower() for w in nltk.word_tokenize(text)]))
       17    0.000    0.000    0.005    0.000 re.py:144(sub)
       17    0.000    0.000    0.000    0.000 re.py:226(_compile)
       22    0.000    0.000    0.000    0.000 re.py:248(_compile_repl)
       22    0.000    0.000    0.001    0.000 re.py:268(_subx)
       71    0.001    0.000    0.003    0.000 re.py:274(filter)
       71    0.002    0.000    0.003    0.000 sre_parse.py:790(expand_template)
        1    0.000    0.000    0.006    0.006 treebank.py:65(tokenize)

>>> profile.run("""type(w.lower() for w in nltk.word_tokenize(text))""")
         506 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       39    0.000    0.000    0.000    0.000 :0(get)
      141    0.001    0.000    0.001    0.000 :0(group)
       71    0.000    0.000    0.000    0.000 :0(join)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000    0.000    0.000 :0(split)
        1    0.000    0.000    0.000    0.000 :0(strip)
       27    0.001    0.000    0.005    0.000 :0(sub)
        1    0.000    0.000    0.000    0.000 <string>:1(<genexpr>)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.006    0.006 __init__.py:80(word_tokenize)
        0    0.000             0.000          profile:0(profiler)
        1    0.000    0.000    0.006    0.006 profile:0(type(w.lower() for w in nltk.word_tokenize(text)))
       17    0.000    0.000    0.005    0.000 re.py:144(sub)
       17    0.000    0.000    0.000    0.000 re.py:226(_compile)
       22    0.000    0.000    0.000    0.000 re.py:248(_compile_repl)
       22    0.000    0.000    0.001    0.000 re.py:268(_subx)
       71    0.001    0.000    0.003    0.000 re.py:274(filter)
       71    0.002    0.000    0.003    0.000 sre_parse.py:790(expand_template)
        1    0.000    0.000    0.006    0.006 treebank.py:65(tokenize)
'''