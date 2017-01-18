#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from collections import OrderedDict

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


def is_stopword(word):
    global stoplist
    return word in stoplist


def feature_vector_baseline(sentence):
    global od, words, stemmer
    od_ = od.copy()
    for word in sentence.split():
        word = stemmer.stem(word)
        if word in words:
            od_[word] = 1
    return od_.values()


stoplist = set(stopwords.words('english'))

stemmer = SnowballStemmer('english')
words = set()
for line in open('data/sentiment.txt'):
    words.update({stemmer.stem(word) for word in line.split()[1:]
                  if not is_stopword(word)})
od = OrderedDict().fromkeys(sorted(words), 0)
