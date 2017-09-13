# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este archivo temporal se encuentra aquí:
C:\Users\Beto\.spyder2\.temp.py
"""
import nltk

colors = 'rgbcmyk' # red,green, blue, cyan, magenta, yellow, black
def bar_chart(categories, words, counts):
    "Plot a bar chart showing counts for each word by category"
    import pylab
    ind = pylab.arange(len(words))
    width = .2
    bar_groups = []
    for c in range(len(categories)):
        bars = pylab.bar(ind+c*width, counts[categories[c]], width, 
                         color=colors[c % len(colors)])
        bar_groups.append(bars)
    pylab.xticks(ind+width, words)
    pylab.legend([b[0] for b in bar_groups], categories,loc='upper left')
    pylab.ylabel('Frequency')
    pylab.title('Frequency of Six Modal Verbs by Genre')
    pylab.show()
    
genres = ['news','religion','hobbies','government','adventure']
modals = ['can','could','may','might','must','will']
    
cfdist = nltk.ConditionalFreqDist( (genre, word) 
                                   for genre in genres
                                   for word in nltk.corpus.brown.words(categories=genre)
                                   if word in modals)
                                       
counts = {} #se debe definir de esta forma no esta nulo
for genre in genres:
    counts[genre] = [cfdist[genre][word] for word in modals]
                                       
bar_chart(genres, modals, counts)
