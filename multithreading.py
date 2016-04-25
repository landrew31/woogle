from redis_queue_controller import RedisQueue
import redis, time, threading
from parser import getUrls, getHtml
from search import saveToElastic, isArticleInDB

THREADS = 100
TOTAL = 0
REDIS = redis.StrictRedis(host='localhost', port=6379, db=0)
QUEUE = RedisQueue('URLS')

class ArticlesParse (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):
        print "Starting " + str(self.threadID)
        self.forever()
        print "Exiting " + str(self.threadID)
    def forever(self):
        while not QUEUE.empty():
            url = QUEUE.get()
            proccessArticle(url)     
def proccessArticle(url):
    if(isArticleInDB(url)):
        return 1
    if(REDIS.get(url)):
        return 2
    else:
        REDIS.set(url, True)      
    html = getHtml(url)
    all_urls = getUrls(html)
    for url in all_urls:
        QUEUE.put(url)
    saveToElastic(html, url)
    REDIS.incr('TOTAL')   

    return 0


def startProcess(numThreads=THREADS):
    for i in range(numThreads):
        thread = ArticlesParse(i)
        thread.start()
        time.sleep(0.01)


def printUrls_fromUrl(url):
    urls = getUrls(getHtml(url))
    print urls



