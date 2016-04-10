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
	new_text = ''
	for p in text:
		new_text += p.get_text()
	clear_text = re.sub("\[\d+\]", '', new_text)
	return clear_text
