from datetime import datetime
from elasticsearch import Elasticsearch
from pprint import pprint
from tagger import getTags
from parser import getTextFromUrl, getUrls, getHtml
# print getTextFromUrl('/wiki/Astronomy');

def getObj(url):
	return getTags(getTextFromUrl(url))

es = Elasticsearch()
# urls = getUrls(getHtml('/wiki/Astronomy'))
# print len(urls)
# for url in urls:
# 	# getObj(url)
# 	es.index(index="articles", doc_type="data", body=getObj(url))
# 	print urls.index(url) 
# es.index(index="articles", doc_type="data", body={"any": "data", "timestamp": datetime.now()})
# print getObj('/wiki/Astronomy')
# es.index(index="articles", doc_type="data", body=getObj('/wiki/Astronomy'))
# print getTags(str(getTextFromUrl('/wiki/History_of_the_United_States')))
# print getTags(str(getTextFromUrl('/wiki/Ernest_Hemingway')))

def search_art(text):
	tags = text.split(" ")
	search_obj = \
	{
	   "query": {
	      "bool": {
	         "should": [
	            {
	               "function_score": {
	                  "query": {
	                     "match": {
	                        "tags": text
	                     }
	                  },
	                  "functions": [
	                     {
	                        "script_score": {
	                           "script": {
	                              "lang": "groovy",
	                              "file": "calculate-score",
	                              "params": {
	                                 "my_tags": tags
	                              }
	                           }
	                        }
	                     }
	                  ]
	               }
	            },
	            {
	               "match": {
	                  "title": {
	                     "query": text,
	                     "boost": 3
	                  }
	               }
	            },
	            {
	               "match": {
	                  "text": {
	                     "query": text,
	                     "boost": 1
	                  }
	               }
	            }
	         ]
	      }
	   }
	}
	res = es.search(index="articles", doc_type="data", body=search_obj)
	pprint(res)
search_art("three body problem")	