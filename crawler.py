"""Crawl web pages given a URL list.

This library is used to crawl web pages using the parser to extract links
It is part of the language processing project.
"""
from parserutils import Parser
import urllib

__author__ = 'nv'

class Crawler:
    def __init__(self, filename=["http://www.ceid.upatras.gr/"]):
        self.queue = filename
        self.notes = {}
        #links = [[i, "", ] for i in seed]

    def crowl(self):
        link = self.queue.pop()
        #for link in nea:
        #one_level
        f = open("crowler.log", "a")
        f.write(link)
        usock = urllib.urlopen(link)
        parser = Parser()
        source = usock.read()
        if source.__len__() > 10:
            f.write(" [" + str(source.__len__()) + "]  * \n")
        parser.feed(source) # parses all the html source
        parser.close()
        usock.close()
        for url in parser.urls:
            #make use of regular expressions
            if 'http' not in url:
                url = link + url
            if url not in self.queue:
                ###8a kanw push ta link pou prepei
                self.queue.append(url)
                f.write(url + "\n")
        f.close()

    def status(self):
       print "\n".join(["%s" % (k,) for k in self.queue])
       # the same for notes [["%s: %s" % (k,v) for k,v in notes.items()]


if __name__ == "__main__":
    seed = ["http://www.ceid.upatras.gr/", "http://www.catonmat.net/"] # "http://www.catb.org/~esr/",
    spider = Crawler(seed)
    spider.crowl()
    spider.status()
    spider.crowl()
    spider.status()
