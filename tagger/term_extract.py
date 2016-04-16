from topia.termextract import extract
import re
extractor = extract.TermExtractor()
TEXT_LEN = 600
NUM_TAGS = 100
def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

def remove_non_ascii_2(text):
    return re.sub(r'[^\x00-\x7F]+',' ', text)

def getTags(obj):
	text = str(remove_non_ascii_2(remove_non_ascii_1(obj['text'])))
	tags = sorted(extractor(text), key=lambda x: x[1], reverse=True)
	length = min(len(tags), NUM_TAGS)
	sum_tag = ''	
	for tag in tags[:length]:
		sum_tag += tag[0] + ' '
	obj['tags'] = sum_tag
	obj['text'] = text[:TEXT_LEN]
	return obj