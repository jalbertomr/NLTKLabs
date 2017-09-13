# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 19:49:20 2014
2_1AccessingTextCorpora
@author: Beto
"""


import nltk
nltk.corpus.gutenberg.fileids()

"""
['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt',
'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 
'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
"""

emma =  nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
#192427

from nltk.corpus import gutenberg
gutenberg.fileids()
#['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']

for fileid in gutenberg.fileids():
     num_chars = len(gutenberg.raw(fileid))
     num_words = len(gutenberg.words(fileid))
     num_sents = len(gutenberg.sents(fileid))
     num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
     print int(num_chars/num_words), int(num_words/num_sents),int(num_words/num_vocab), fileid

""" 
4 21 26 austen-emma.txt
4 23 16 austen-persuasion.txt
4 23 22 austen-sense.txt
4 33 79 bible-kjv.txt
4 18 5 blake-poems.txt
4 17 14 bryant-stories.txt
4 17 12 burgess-busterbrown.txt
4 16 12 carroll-alice.txt
4 17 11 chesterton-ball.txt
4 19 11 chesterton-brown.txt
4 16 10 chesterton-thursday.txt
4 17 24 edgeworth-parents.txt
4 24 15 melville-moby_dick.txt
4 52 10 milton-paradise.txt
4 11 8 shakespeare-caesar.txt
4 12 7 shakespeare-hamlet.txt
4 12 6 shakespeare-macbeth.txt
4 35 12 whitman-leaves.txt
"""

macbeth_sentences =gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
#[['[', 'The', 'Tragedie', 'of', 'Macbeth', 'by', 'William', 'Shakespeare', '1603', ']'], ['Actus', 'Primus', '.'], ...]

from nltk.corpus import webtext
for fileid in webtext.fileids():
     print fileid, webtext.raw(fileid)[:65]
""" 
firefox.txt Cookie Manager: "Don't allow sites that set removed cookies to se
grail.txt SCENE 1: [wind] [clop clop clop] 
KING ARTHUR: Whoa there!  [clop
overheard.txt White guy: So, do you have any plans for this evening?
Asian girl
pirates.txt PIRATES OF THE CARRIBEAN: DEAD MAN'S CHEST, by Ted Elliott & Terr
singles.txt 25 SEXY MALE, seeks attrac older single lady, for discreet encoun
wine.txt Lovely delicate, fragrant Rhone wine. Polished leather and strawb
"""

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]
#['i', 'do', "n't", 'want', 'hot', 'pics', 'of', 'a', 'female', ',', 'I', 'can', 'look', 'in', 'a', 'mirror', '.']
 
from nltk.corpus import brown
brown.categories()
#['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
brown.words(categories='news')
#['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
brown.words(fileids=['cg22'])
#['Does', 'our', 'society', 'have', 'a', 'runaway', ',', ...]
brown.sents(categories=['news','editorial','reviews'])
#[['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', 'Friday', 'an', 'investigation', 'of', "Atlanta's", 'recent', 'primary', 'election', 'produced', '``', 'no', 'evidence', "''", 'that', 'any', 'irregularities', 'took', 'place', '.'], ['The', 'jury', 'further', 'said', 'in', 'term-end', 'presentments', 'that', 'the', 'City', 'Executive', 'Committee', ',', 'which', 'had', 'over-all', 'charge', 'of', 'the', 'election', ',', '``', 'deserves', 'the', 'praise', 'and', 'thanks', 'of', 'the', 'City', 'of', 'Atlanta', "''", 'for', 'the', 'manner', 'in', 'which', 'the', 'election', 'was', 'conducted', '.'], ...]

from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist=nltk.FreqDist([w.lower() for w in news_text])
modals = ['can','could','may','might','must','will']
for m in modals:
    print m + ':',fdist[m]
""" 
can: 94
could: 87
may: 93
might: 38
must: 53
will: 389
"""
 
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

genres=['news','religion','hobbies','science_fiction','romance','humor']
modals=['can','could','may','might','must','will']
cfd.tabulate(conditions=genres, samples=modals)
"""
                 can could  may might must will
           news   93   86   66   38   50  389
       religion   82   59   78   12   54   71
        hobbies  268   58  131   22   83  264
science_fiction   16   49    4   12    8   16
        romance   74  193   11   51   45   43
          humor   16   30    8    8    9   13
""" 

from nltk.corpus import inaugural
inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]

cfd = nltk.ConditionalFreqDist(
     (target, fileid[:4])
     for fileid in inaugural.fileids()
     for w in inaugural.words(fileid)
     for target in  ['america','citizen']
     if w.lower().startswith(target))
 
cfd.plot()