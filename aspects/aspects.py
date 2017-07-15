#!/usr/bin/env python3
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from collections import Counter
import string

import helpers

class Aspects:

    wordTokens = []

    def __init__(self):
        self.setReviews()
        self.wordTokenize()
        self.filterStopWords()
        self.applyLemmatizing()


    def tf(self, n=2):
        '''Calculate term frequency'''
        count = Counter(list(ngrams(self.wordTokens, n))) if n > 1 else Counter(self.wordTokens)
        print(count.most_common(100))


    def setReviews(self):
        '''Set revires for single products as list'''
        self.reviews = helpers.getSingleProductReviews("0528881469")


    def wordTokenize(self):
        '''Tokenize words'''
        tokenizer = RegexpTokenizer(r'\w+')
        [self.wordTokens.extend(tokenizer.tokenize(review.lower())) for review in self.reviews]

        # Tokenize using word_tokenize
        #[self.wordTokens.extend(word_tokenize(review.lower())) for review in self.reviews]

        # Count words and store as dict
        #self.wordsCount = dict(Counter(self.wordTokens))


    def filterStopWords(self):
        self.wordTokens = [word for word in self.wordTokens if not word in stopwords.words('english')]
        # Apply filter to dict
        #self.wordsCount = {word: count for (word, count) in self.wordsCount.items() if not word in stopwords.words('english')}


    def filterPunctuation(self):
        self.wordTokens = [word for word in self.wordTokens if not word in [p for p in string.punctuation]]
        # Apply filter to dict
        #self.wordsCount = {word: count for (word, count) in self.wordsCount.items() if not word in [p for p in string.punctuation]}


    def applyLemmatizing(self):
        lemmatizer = WordNetLemmatizer()
        self.wordTokens = [lemmatizer.lemmatize(word) for word in self.wordTokens]
        # Apply to dict
        #maps = {word: lemmatizer.lemmatize(word) for (word, count) in self.wordsCount.items()}
        #self.combindSimilar(maps)


    def combindSimilar(self, maps):
        '''Add values for similar keys'''
        reduced = {}
        for name, count in self.wordsCount.items():
            maped = maps[name]
            if not maped in reduced:
                reduced[maped] = count
            else:
                reduced[maped] = reduced[maped] + count
        self.wordsCount = reduced


if __name__ == "__main__":
    a = Aspects()
    a.tf()