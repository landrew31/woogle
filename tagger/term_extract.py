from topia.termextract import extract
extractor = extract.TermExtractor()
TEXT_LEN = 600
NUM_TAGS = 100
def getTags(obj):
	text = str(obj['text'])
	tags = sorted(extractor(text), key=lambda x: x[1], reverse=True)
	length = min(len(tags), NUM_TAGS)
	sum_tag = ''	
	for tag in tags[:length]:
		sum_tag += tag[0] + ' '
	obj['tags'] = sum_tag
	obj['text'] = text[:TEXT_LEN]
	return obj