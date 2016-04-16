import threading
from sets import Set
from Queue import Queue
from parser import getUrls, getHtml
from search import saveToElastic, isArticleInDB
URLS = []
EXEC = Set([])
TOTAL = 0

print_lock = threading.Lock()

class ArticlesParse (threading.Thread):
    def __init__(self, threadID, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.url = url
    def run(self):
        print "Starting " + str(self.threadID)
        proccessArticle(self.url, self.threadID)
        self.forever()
        print "Exiting " + str(self.threadID)
    def forever(self):
        while len(URLS):
            url = URLS.pop()
            proccessArticle(url, self.threadID)  
def proccessArticle(url, threadID):
    global TOTAL 
    global URLS 
    if(isArticleInDB(url)):
        return 1
    if(url in EXEC):
        return 2
    else:
        EXEC.add(url)     
    html = getHtml(url)
    all_urls = getUrls(html)
    URLS += all_urls
    saveToElastic(html, url)
    EXEC.remove(url) 
    TOTAL += 1  
    with print_lock:
        print TOTAL
    return 0

def printUrls_fromUrl(url):
    urls = getUrls(getHtml(url))
    print urls


