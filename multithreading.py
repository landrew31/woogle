import threading
from sets import Set
from Queue import Queue
from parser import getUrls, getHtml
from search import saveToElastic, isArticleInDB
URLS = []
EXEC = Set([])
TOTAL = 0

print_lock = threading.Lock()


q = Queue()
    


# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        url = q.get()

        # Run the example job with the avail worker in queue (thread)
        proccessArticle2(url)

        # completed with the job
        q.task_done()



        

# for x in range(30):
#      t = threading.Thread(target=threader)

#      # classifying as a daemon, so they will die when the main dies
#      t.daemon = True

#      # begins, must come after daemon definition
#      t.start()

def proccessArticle2(url):
    global TOTAL 
    if(isArticleInDB(url)):
        return 1
    if(url in EXEC):
        return 2
    else:
        EXEC.add(url)     
    html = getHtml(url)
    all_urls = getUrls(html)
    for new_url in all_urls:
        q.put(new_url)
    saveToElastic(html, url)
    EXEC.remove(url) 
    TOTAL += 1  
    with print_lock:
        print TOTAL
    return 0
'''
urls = ['/wiki/History_of_the_United_States', '/wiki/Ernest_Hemingway', '/wiki/Jupiter', '/wiki/Astronomy_in_medieval_Islam', '/wiki/Radio_astronomy', '/wiki/Tibetan_astronomy', '/wiki/Reionization', '/wiki/Aristarchus_of_Samos', '/wiki/Stellar_nucleosynthesis', '/wiki/Tidal_acceleration', '/wiki/CRC_Press', '/wiki/Hubble_Space_Telescope', '/wiki/Joseph_Louis_Lagrange', '/wiki/Wave', '/wiki/Astrophotography', '/wiki/Gravitational_waves', '/wiki/Sidewalk_astronomy', '/wiki/Encyclopedia_of_the_History_of_Arabic_Science', '/wiki/Interstellar_dust', '/wiki/Volcanism', '/wiki/Observational_astronomy', '/wiki/Near-ultraviolet', '/wiki/Cosmogony', '/wiki/Apparent_magnitude', '/wiki/Chronology_of_the_Universe', '/wiki/Keck_Observatory', '/wiki/Electron', '/wiki/Bremsstrahlung_radiation', '/wiki/Slovakia', '/wiki/Amateur_telescope_making', '/wiki/Natural_satellite', '/wiki/Big_bang', '/wiki/Very_Large_Array', '/wiki/Precession', '/wiki/Planetary_differentiation', '/wiki/Glossary_of_astronomy', '/wiki/Neptune', '/wiki/Population_III_stars', '/wiki/Fine-tuned_universe', '/wiki/Chinese_astronomy', '/wiki/Ja%27far_ibn_Muhammad_Abu_Ma%27shar_al-Balkhi', '/wiki/Gravitation', '/wiki/Gamma-ray_astronomy', '/wiki/Circumstellar_disk', '/wiki/Chambers_Book_of_Days']
print len(urls)
# 100 jobs assigned.
for url in urls:
    q.put(url)

# wait until the thread terminates.
q.join()

'''
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

# proccessArticle('/wiki/Astronomy', 1)
# urls = getUrls(getHtml('/wiki/Geography_of_China'))
# print urls
