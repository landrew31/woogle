from elasticsearch import Elasticsearch
from pprint import pprint
from tagger import getTags
from parser import getTextFromHtml






def saveToElastic(html, url):
	text = getTextFromHtml(html, url)
	tags = getTags(text)
	es = Elasticsearch()
	es.index(index="articles", doc_type="data", body=tags)

def isArticleInDB(url):
	es = Elasticsearch()
	res = es.search(index="articles", doc_type="data", body={"query": {"match": {"url.raw": url}}})
	return res['hits']['total'] > 0


def initEs():
	es = Elasticsearch()
	es.indices.delete(index="articles", ignore=[400, 404])
	index_body = \
	{
	  "mappings": {
	    "data": {
	      "properties": {
	        "url" : {
	          "type": "string",
	          "fields": {
	            "raw" : {
	              "type": "string",
	              "index": "not_analyzed"
	            }
	          }
	        }
	      }
	    }
	  }
	}
	es.indices.create(index="articles", body=index_body, ignore=[400])

def search_art(text):
	es = Elasticsearch()
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


# search_art("oxygen molecule")	


