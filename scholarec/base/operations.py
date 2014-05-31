# -*- coding: utf-8 -*- 

## This file is part of ScholaRec.
## A recommendation engine for Scholarly works.
## Copyright (C) 2014  Archit Sharma <archit.py@gmail.com>
##
## ScholaRec is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## ScholaRec is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>

""" This script processes the respective data structures, 
passed to the object of Document Class and returns new information
such as topwords."""

from nltk import \
    word_tokenize,\
    PorterStemmer,\
    word_tokenize
    #LancasterStemmer
from nltk.corpus import stopwords

import string
#from collections import Counter

class DocumentOperations(object):
    """
    Perform all kinds of operations on the 
    plain text documents in the db."""
    
    def __init__(self, db_path):
        self.path = db_path
        
    def search(self, stopwords, keywords):
        """
        Search for keywords among 
        plain text files.
        """
        pass

    def stemmer(self, raw):
        """
        Use porter stemmer from nltk library 
        to stem tokens in raw text.
        """
        tokens = word_tokenize(raw)
        porter = PorterStemmer()
        # lancaster = LancasterStemmer()
        # stem_lancaster = [lancaster.stem(t) for t in tokens]
        stem_porter = [porter.stem(t) for t in tokens]
        return stem_porter
    '''
    def get_tokens(self):
       with open(self.path, 'r') as shakes:
        text = shakes.read()
        lowers = text.lower()
        #remove the punctuation using the character deletion step of translate
        no_punctuation = lowers.translate(None, string.punctuation)
        tokens = nltk.word_tokenize(no_punctuation)
        return tokens
    '''
    '''
    tokens = get_tokens()
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    count = Counter(filtered)
    print count.most_common(100)
    '''
