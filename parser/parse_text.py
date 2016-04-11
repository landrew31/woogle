# -*- coding: utf-8 -*-
from send_request import getHtml
from bs4 import BeautifulSoup
import sys, re
reload(sys)
sys.setdefaultencoding('utf8')


def getTextFromUrl(url):
	html_doc = getHtml(url)
	soup = BeautifulSoup(html_doc, 'html.parser')
	text = soup.find_all("p")
	try:
		title = soup.select("#firstHeading")[0].get_text()
	except:
		title = ''	
	new_text = ''
	for p in text:
		new_text += p.get_text()
	clear_text = re.sub("\[\d+\]", '', new_text)
	return {"text": clear_text, "title": title, "url": url}


# print getTextFromUrl('/wiki/Astronomy')