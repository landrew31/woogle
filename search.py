from datetime import datetime
from elasticsearch import Elasticsearch
from tagger import getTags
from parser import getTextFromUrl, getUrls, getHtml
# print getTextFromUrl('/wiki/Astronomy');

def getObj(url):
	return getTags(getTextFromUrl(url))

es = Elasticsearch()
urls = getUrls(getHtml('/wiki/Astronomy'))
print len(urls)
for url in urls:
	getObj(url)
	# es.index(index="articles", doc_type="data", body=getObj(url))
	print urls.index(url) 
# es.index(index="articles", doc_type="data", body={"any": "data", "timestamp": datetime.now()})
# print getObj('/wiki/Astronomy')
# es.index(index="articles", doc_type="data", body=getObj('/wiki/Astronomy'))
# print getTags(str(getTextFromUrl('/wiki/History_of_the_United_States')))
# print getTags(str(getTextFromUrl('/wiki/Ernest_Hemingway')))