from tagger import getTags
from parser import getTextFromUrl
# print getTextFromUrl('/wiki/Astronomy');
print getTags(getTextFromUrl('/wiki/Astronomy'))