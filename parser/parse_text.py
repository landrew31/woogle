# -*- coding: utf-8 -*-
from send_request import getHtml
import sys, re
reload(sys)
sys.setdefaultencoding('utf8')


def getTextFromHtml(html_doc, url):
	
	text = re.findall('<p>(.*)</p>', html_doc) 
	try:
		title = re.findall('id="firstHeading"[^>]*>([^<]*)<', html_doc)[0]
	except:
		title = ''
	new_text = ''
	for p in text:
		new_text += re.sub("(<[^<]*>)", '', p);
	clear_text = re.sub("\[\d+\]", '', new_text)
	return {"text": clear_text, "title": title, "url": url}


# print getTextFromHtml(getHtml('/wiki/Astronomy'), '/wiki/Astronomy')['title']