"""A Web Page class implementing single-page stats and functions.


"""

__author__ = 'nv'

class Page:
    numberOfPages = 0

    def __init__(self,link):
        self.__class__.numberOfPages += 1
        self.url = link
        stripURL = link.rindex("/")

    def output(self):
        print self.numberOfPages, " | "

if __name__ == "__main__":
    print "starting..."
    ena = Page("http://www.ceid.upatras.gr")
    ena.output()
    duo = Page("http://www.mozilla.com/en-US/firefox/central/")
    duo.output()
    print "ending.."