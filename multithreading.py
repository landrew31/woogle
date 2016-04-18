
import redis, time, threading, multiprocessing
from parser import getUrls, getHtml
from search import saveToElastic, isArticleInDB, initEs

WRITE = 10
THREADS = 1000
PROCESS = 1
TOTAL = 0
EXEC = redis.StrictRedis(host='localhost', port=6379, db=0)

print_lock = threading.Lock()

class ArticlesParse (threading.Thread):
    def __init__(self, URLS, threadID, processID, TOTAL):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.processID = processID
        self.URLS = URLS
        self.TOTAL = TOTAL
    def run(self):
        print "Process " + str(self.processID) + "Starting " + str(self.threadID)
        self.forever()
        print "Process " + str(self.processID) + "Exiting " + str(self.threadID)
    def forever(self):
        while not self.URLS.empty():
            url = self.URLS.get()
            proccessArticle(url, self.URLS, self.TOTAL)     
def proccessArticle(url, URLS, TOTAL):
    if(isArticleInDB(url)):
        return 1
    if(EXEC.get(url)):
        return 2
    else:
        EXEC.set(url, True)      
    html = getHtml(url)
    all_urls = getUrls(html)
    for url in all_urls:
        URLS.put(url)
    saveToElastic(html, url)
    TOTAL.value += 1 
    if(TOTAL.value % WRITE == 0): 
        with print_lock:
            print TOTAL.value
    return 0


def startProcess(URLS, numThreads, processID, TOTAL):
    for i in range(numThreads):
        thread = ArticlesParse(URLS, i, processID, TOTAL)
        thread.start()
        time.sleep(0.01)

def startApp(urls):
    URLS = multiprocessing.Queue() 
    initEs()
    EXEC.flushdb()
    TOTAL = multiprocessing.Value('I', 0)
    for url in urls:
        URLS.put(url)
    time.sleep(0)    
    for ID in range(PROCESS):
        Process = multiprocessing.Process(target=startProcess, args=(URLS, THREADS, ID, TOTAL, ))    
        Process.start()

def printUrls_fromUrl(url):
    urls = getUrls(getHtml(url))
    print urls


