"""Crawl web pages given a URL list.

This library is used to crawl web pages using the parser to extract links
It is part of the language processing project.

TODO: Implement asynchronous crawling or somehow threading -->
http://oubiwann.blogspot.com/2008/06/async-batching-with-twisted-walkthrough.html
"""
from page import Page
from parserutils import Parser
import urllib2

__author__ = 'nv'

class Crawler:
    def __init__(self, filename=["http://www.ceid.upatras.gr/"]):
        self.queue = filename
        self.history = filename
        self.notes = {}
        #links = [[i, "", ] for i in seed]

    def crawl(self):
        """ The crawling is done in two phases after the URL pops from the queue
        1. Add URL with some info to notes (if source is more than 40k chars incl. html)
        2. Push children URLs to queue if they pass all crawling validations

        """
        link = self.queue.pop(0)
        #for link in nea:
        #one_level
        f = open("crawler.log", "a")
        f.write("+++++++++++" + link)
        # todo implement timeout!!!
        request = urllib2.Request(link)
        opener = urllib2.build_opener()

        # source = urllib.urlopen(link).read()
        parser = Parser()
        source = opener.open(request, timeout=2).read()
        parser.feed(source) # parses all the html source
        parser.close()
        opener.close()
        if source.__len__() > 1000:  # Change page character limit
            f.write(" [" + str(source.__len__()) + "]  * \n")
            self.notes[link]="working"
            webPage = Page(link, source)
            webPage.flash()
            #webPage.flashTkn()
        for url in parser.urls:
            if 'http' not in url:
               url = link + url
            if url not in self.history:
                self.queue.append(url)
                self.history.append(url)
                f.write(url + "\n")
        f.close()

    def status(self):
       print "\n".join(["%s" % (k,) for k in self.queue])
       # the same for notes [["%s: %s" % (k,v) for k,v in notes.items()]
       print "\n\n --------- \n\n"
       print "\n".join(["%s: %s" % (k,v) for k,v in self.notes.items()])

    def keep_crawling(self):
        # change length of notes to adjust time of execution
        if self.notes.__len__() < 100:
            return True;


if __name__ == "__main__":
    print " *** Be sure to create a 'local' subdir ***"
    print " *** TODO: Implement Timeout: 2 seconds ***"
    seed = ["http://www.ceid.upatras.gr/", "http://www.python.org/"] # "http://www.catb.org/~esr/",
    spider = Crawler(seed)
    while spider.keep_crawling():
        spider.crawl()
    spider.status()
