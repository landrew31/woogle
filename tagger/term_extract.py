# -*- coding: utf-8 -*-

import tagger, pickle
from tagger import Tagger
import string
import re
printable = set(string.printable)

TAGS_NUM = 20

weights = pickle.load(open('tagger/data/dict.pkl', 'rb')) 
myreader = tagger.Reader() 
mystemmer = tagger.Stemmer() 
myrater = tagger.Rater(weights)
mytagger = Tagger(myreader, mystemmer, myrater)

def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

def remove_non_ascii_2(text):
    return re.sub(r'[^\x00-\x7F]+',' ', text)

def getTags(text):
	text = remove_non_ascii_1(text)
	text = remove_non_ascii_2(text)
	filter(lambda x: x in printable, text)
	return mytagger(text, TAGS_NUM)
