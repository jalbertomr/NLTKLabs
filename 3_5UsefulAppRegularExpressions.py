# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 18:05:42 2014
3_5UsefulAppRegularExpressions
@author: Beto
"""

import re
import nltk

word = 'supercalifragilisticoespinalidoso'
print (re.findall('[aeiou]', word))

#look for all sequences of two or more vowels in some text, and
#determine their relative frequency
#first get word from corpus, from interactive terminal
#>>> nltk.corpus.treebank.words()
#>>>['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', ...]
#but how much words are they
#>>> len(nltk.corpus.treebank.words())
#>>> 100676
#>>> well, but how we can eliminate de repeated words
#>>> len(set(nltk.corpus.treebank.word()))
#>>> 12408
#>>> almost 10% lower
#Aditionaly we can sort it with 
#>>> sorted(set(...))

#create our wordlist
wordlist = nltk.corpus.treebank.words()

# lets build our occurences in the word list
for word in wordlist:
    foundOcur = re.findall('[aeiou]{2,}', word) #return a list of ocurrences
    print word, foundOcur
#...    
#quiet ['uie']
#quietly ['uie']
#quipped ['ui']
#quips ['ui']
#quite ['ui']
#quitting ['ui']
#quota ['uo']
#quotas ['uo']
#quotations ['uo', 'io']
#quote ['uo']
#quoted ['uo']
#quoting ['uo']
#race []
#raced []
#races [] ...

# Lets get the occurences pattern in the word list
#   iter-element list-iterated
for word      in wordlist:
    #   iter-ele    list of occurrences in a word
    # with for we separate each occurence in word
    for foundOcur in re.findall('[aeiou]{2,}', word):
        print foundOcur,
#ea oi ea ou oi ea ea oi oi ea io ea ea ea oi ea ea ea ea ea ea ea ee ea ea ea ea ea ea ea ea oi ea ea
        
for word in wordlist:
    for foundOcur in re.findall('[aeiou]{2,}', word):
        foundOcur
#'ea'
#'oi'
#'ea'
#'ou'
#'oi'
#'ea'...

#The previous can be inserted in a list and in one line of code        
[foundOcur for word in wordlist for foundOcur in re.findall('[aeiou]{2,}', word)]
#['ea', 'oi', 'ea', 'ou', 'oi', 'ea', 'ea', 'oi', 'oi', 'ea', 'io', 'ea', 'ea', 'ea', 'oi', 'ea', 'ea', 'ea', 'ea', 'ea', 'ea', 'ea', 'ee', 'ea', 'ea', 'ea', 'ea', 'ea', 'ea', 'ea', 'ea', 'oi', 'ea', 'ea', 'ou', 'ou', 'ou', 'ie', 'ui', 'io', 'ua', 'io', 'ai', 'ai', 'ai', 'io', 'ie', 'ue', 'ue', 'ia', 'ie', 'ea', 'ai', 'ou', 'ia', 'ei', 'ie', 'ea', 'ea', 'ie', 'ia', 'ia', 'ua', 'ie', 'io', 'ea',...
[word for word in wordlist for foundOcur in re.findall('[aeiou]{2,}', word)]
#['10-year', '12-point', '12-year', '14-hour', '150-point', '17-year-old', '18-year-old', '190-point', '20-point', '237-seat', '238,000-circulation', '25-year-old', '27-year', '29year', '30-point', '30-year', '31-year-old', '37-year-old', '40-year-old', '42-year', '43-year-old', '51-year-old', '52-week', '53-year-old', '54-year-old', '55-year-old',...

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist( vs for word in wsj
                       for vs in re.findall('[aeiou]{2,}', word))
                           
#>>> fd
#<FreqDist with 43 samples and 3405 outcomes>                           
print fd
#<FreqDist: 'io': 549, 'ea': 476, 'ie': 331, 'ou': 329, 'ai': 261, 'ia': 253, 'ee': 217, 'oo': 174, 'ua': 109, 'au': 106, ...>                           
                 
print fd.items
#<bound method FreqDist.items of <FreqDist with 43 samples and 3405 outcomes>>                 
print fd.items()
#[('io', 549), ('ea', 476), ('ie', 331), ('ou', 329), ('ai', 261), ('ia', 253),                
print fd.keys()
#['io', 'ea', 'ie', 'ou', 'ai', 'ia', 'ee', 'oo', 'ua', 'au', 'ue', 'ui', 'ei', 'oi', 'oa', 'eo', 'iou', 'eu', 'oe', 'iu', 'ae', 'eau', 'uo', 'ao', 'oui',...
print fd.values()
#[549, 476, 331, 329, 261, 253, 217, 174, 109, 106, 105, 95, 86, 65, 59, 39, 27, 18, 15, 14, 11, 10, 8, 6, 6, 5, 5, 4, 3, 3, 3, 2, 1, 1, 1, 1, 1,...

#Replace ? in order to convert the string '2009-12-31' to a list of integers [2009,12,31]
#[int(n) for n in re.findall(?,'2009-12-31')]
print [int(n) for n in re.findall('[0-9]+','2009-12-31')]
#[2009, 12, 31]

print [int(n)+1 for n in re.findall('[0-9]+','2009-12-31')]
#[2010, 13, 32]

#Doing more with word PIECES
word = 'supercalifragilisticoespinalidoso'
regexp = '^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
#['s', 'p', 'r', 'c', 'l', 'f', 'r', 'g', 'l', 's', 't', 'c', 's', 'p', 'n', 'l', 'd', 's', 'o']
# ''.join()
print ''.join(re.findall(regexp, word))
#'sprclfrglstcspnldso'

regexp = '^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
def compress( word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)
    
english_udhr = nltk.corpus.udhr.words('English-Latin1')
print nltk.tokenwrap(compress(w) for w in english_udhr[:75])
#Unvrsl Dclrtn of Hmn Rghts Prmble Whrs rcgntn of the inhrnt dgnty and
#of the eql and inlnble rghts of all mmbrs of the hmn fmly is the fndtn
#of frdm , jstce and pce in the wrld , Whrs dsrgrd and cntmpt fr hmn
#rghts hve rsltd in brbrs acts whch hve outrgd the cnscnce of mnknd ,
#and the advnt of a wrld in whch hmn bngs shll enjy frdm of spch and   

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate(cvs)
#     a    e    i    o    u
#k  418  148   94  420  173
#p   83   31  105   34   51
#r  187   63   84   89   79
#s    0    0  100    2    1
#t   47    8    0  148   37
#v   93   27  105   48   49

#create a list of tuples, word-pairs
cv_word_pairs = [ (w,cv) for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
#[('kaa', 'ka'), ('kaa', 'ka'), ('kaa', 'ka'), ('kaakaaro', 'ka'), ('kaakaaro', 'ka'), ('kaakaaro', 'ro'), ('kaakaaviko', 'ka'), ('kaakaaviko', 'ka'),

cv_word_pairs[3]
#('kaakaaro', 'ka')
cv_word_pairs[3][0]
#'kaakaaro'
cv_word_pairs[3][1]
#'ka'
#cv_word_pairs[3][2]
#Error tuple index out of range

#well, sorry  lest order the list in correct order pair
cv_word_pairs = [(cv, w) for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)] 
#[('ka', 'kaa'), ('ka', 'kaa'), ('ka', 'kaa'), ('ka', 'kaakaaro'), ('ka', 'kaakaaro'), ('ro', 'kaakaaro'), ('ka', 'kaakaaviko'), ('ka', 'kaakaaviko'), ('vi', 'kaakaaviko'), ('ko', 'kaakaaviko'), ('ka', 'kaakaavo'),

cv_index = nltk.Index(cv_word_pairs)
cv_index
#defaultdict(<type 'list'>, {'va': ['kaaova', 'Kaareva', 'kaava', 'kaavaaua', 'kakuva', 'kapaava', 'karaava', 'karaova', 'karavau', 'karekarererava', 'karekova', 'kariava', 'karivai', 'karivaito', 'karivara',...], 've':[...], 'vi':[...]...]})
cv_index['su']
#['kasuari']
cv_index['po']
#['kaapo', 'kaapopato', 'kaipori', 'kaiporipie', 'kaiporivira', 'kapo', 'kapoa', 'kapokao', 'kapokapo', 'kapokapo', 'kapokapoa', 'kapokapoa', 'kapokapora', 'kapokapora', 'kapokaporo', 'kapokaporo', 'kapokari',...

"""
3_5 finding word stem

  STEM
  word---endings
"""
def stem( word):
    for suffix in ['ing','ly','ed','ious','ies','ive','es','s','ment']:
        if word.endwith(suffix):
            return word[:-len(suffix)]
    return word
    
re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$','processing')    
#['ing']
    
re.findall(r'(ing|ly|ed|ious|ies|ive|es|s|ment)$','processing')
#['ing']

re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$','processing')    
#['processing']
    
re.findall(r'^(.*)(?:ing|ly|ed|ious|ies|ive|es|s|ment)$','processing')
#['process']

re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$','processing')
#[('process', 'ing')]

#greedy  .*
re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$','processes')
#[('processe', 's')]

#non-greedy
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$','processes')
re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|s|es|ment)$','processes')
#[('process', 'es')] 

re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$','language')
#[]

re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$','language')
#[('language', '')]

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem
    
raw = """DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government. Supreme executive power derives from
a mandete from the masses, not from some farcical aquatic ceremony."""

tokens = nltk.word_tokenize(raw)
#>>>tokens
#['DENNIS', ':', 'Listen', ',', 'strange', 'women', 'lying', 'in', 'ponds', 'distributing', 'swords', 'is', 'no', 'basis', 'for', 'a', 'system', 'of', 'government.', 'Supreme', 'executive', 'power', 'derives', 'from', 'a', 'mandete', 'from', 'the', 'masses', ',', 'not', 'from', 'some', 'farcical', 'aquatic', 'ceremony', '.']

[stem(t) for t in tokens]
#['DENNIS', ':', 'Listen', ',', 'strange', 'women', 'ly', 'in', 'pond', 'distribut', 'sword', 'i', 'no', 'basi', 'for', 'a', 'system', 'of', 'government.', 'Supreme', 'execut', 'power', 'deriv', 'from', 'a', 'mandete', 'from', 'the', 'mass', ',', 'not', 'from', 'some', 'farcical', 'aquatic', 'ceremony', '.']
# ponds is basis distributing are produced non-words but acceptable stems in some applications

#Searching tokenized text

from nltk.corpus import gutemberg, nps_chat
moby = nltk.Text(gutemberg.words('melville-moby_dick.txt'))
moby.findall(r'<a><.*><man>')
#a monied man; a nervous man; a dangerous man; a white man; a white
#man; a white man; a pious man; a queer man; a good man; a mature man;
#a white man; a Cape man; a great man; a wise man; a wise man; a
#butterless man; a white man; a fiendish man; a pale man; a furious
#man; a better man; a certain man; a complete man; a dismasted man; a
#younger man; a brave man; a brave man; a brave man; a brave man

#angle brackets are used to mark token boundaries

moby.findall(r"<a> (<.*>) <man>")
#monied; nervous; dangerous; white; white; white; pious; queer; good;
#mature; white; Cape; great; wise; wise; butterless; white; fiendish;
#pale; furious; better; certain; complete; dismasted; younger; brave;
#brave; brave; brave

chat = nltk.Text(nltk.corpus.nps_chat.words())
#tree-word phrases endind with the word bro
chat.findall(r'<.*><.*> <bro>')
#you rule bro; telling you bro; u twizted bro

#sequence of tree or more words starting with letter l
chat.findall(r'<l.*>{3,}')
#lol lol lol; lmao lol lol; lol lol lol; la la la la la; la la la; la
#la la; lovely lol lol love; lol lol lol.; la la la; la la la

#x and other ys
chat.findall(r'<\w*> <and> <other> <\w*s>')
#Whales and other monsters; lances and other weapons; vignettes and
#other embellishments; chains and other necessaries; backs and other
#whales; cattle and other animals

from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies','learned']))
#['Too', 'often', 'a', 'beginning', 'bodybuilder', ...]

hobbies_learned.findall(r'<\w*> <and> <other> <\w*s>')
#speed and other activities; water and other liquids; tomb and other
#landmarks; Statues and other monuments; pearls and other jewels;
#charts and other items; roads and other features; figures and other
#objects; military and other areas; demands and other factors;
#abstracts and other compilations; iron and other metals

hobbies_learned.findall(r'<as> <\w*> <as> <\w*>')
#as accurately as possible; as well as the; as faithfully as possible;
#as much as what; as neat as a; as simple as you; as well as other; as
#well as other; as involved as determining; as well as other; as
#important as another; as accurately as possible; as accurate as any;
#as much as any; as different as a; as Orphic as that; as coppery as ...

#nltk.re_show(regexp, string, left="{", right="}")
nltk.re_show(r'ro',raw)
#DENNIS: Listen, strange women lying in ponds distributing swords
#is no basis for a system of government. Supreme executive power derives f{ro}m
#a mandete f{ro}m the masses, not f{ro}m some farcical aquatic ceremony.

nltk.re_show(r'\n', raw)
#DENNIS: Listen, strange women lying in ponds distributing swords{
#}is no basis for a system of government. Supreme executive power derives from{
#}a mandete from the masses, not from some farcical aquatic ceremony.

nltk.re_show(r'\n',raw,left='_Retorno->',right='<-Retorno_')
#DENNIS: Listen, strange women lying in ponds distributing swords_Retorno->
#<-Retorno_is no basis for a system of government. Supreme executive power derives from_Retorno->
#<-Retorno_a mandete from the masses, not from some farcical aquatic ceremony.

nltk.app.nemo()


