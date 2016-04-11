# -*- coding: utf-8 -*-

import tagger, pickle
from tagger import Tagger
import string
import re
printable = set(string.printable)

TAGS_NUM = 100
TEXT_LEN = 600

weights = pickle.load(open('tagger/data/dict.pkl', 'rb')) 
myreader = tagger.Reader() 
mystemmer = tagger.Stemmer() 
myrater = tagger.Rater(weights)
mytagger = Tagger(myreader, mystemmer, myrater)

def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

def remove_non_ascii_2(text):
    return re.sub(r'[^\x00-\x7F]+',' ', text)

def getTags(obj):
	text = str(obj['text'])
	text = remove_non_ascii_1(text)
	text = remove_non_ascii_2(text)
	filter(lambda x: x in printable, text)
	tags = mytagger(text, TAGS_NUM)
	obj['tags'] = " ".join(map(lambda x: x.string, tags))
	obj['text'] = text[:TEXT_LEN]
	return obj
