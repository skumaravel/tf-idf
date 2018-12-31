# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:09:53 2018

@author: sujeeth.kumaravel
"""

from tf_idf import tf_idf

corpus = []
doc1 = 'do not mess with me'
doc2 = 'if not, that is going to be a damaging experience'
doc3 = 'i will even kill you'
doc4 = 'tomorrow is saturday'
doc5 = 'cooking is done is kitchen. pooping is done in restroom'

corpus.append(doc1)
corpus.append(doc2)
corpus.append(doc3)
corpus.append(doc4)
corpus.append(doc5)

doc = 'tomorrow is saturday'

word= 'tomorrow'

a = tf_idf(corpus, doc, word)
print(a)