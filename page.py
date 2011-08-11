"""A Web Page class implementing single-page stats and functions.


"""

__author__ = 'nv'

class Page:
    numberOfPages = 0

    # We need to pass raw data in order to save local copies.
    def __init__(self, link, rawData=""):
        self.__class__.numberOfPages += 1
        self.url = link
        self.striped = link[7:] # removing http:// link.rindex("/")
        # we cannot have a filename with slashes - we need to alter the
        # name nomeclature based on the final slash
        # (../ba.html or ../ba vs ../ba/)
#        hasEndingSlash = (link[-1]=="/")
#        filenameFunction = hasEndingSlash and (lambda l: l[l[:-1].rindex("/"):]) or (lambda l: l)

        # keep some url characters for the filename and add a unique identifier
        transform = "|".join(self.striped.split("/"))
        transform = (transform[-1]=="|") and transform[:-2] or transform
        transform=  transform.__len__() > 10 and transform[4:5+4] + transform[-5:] or transform
        self.id = transform + "--" + str(self.__class__.numberOfPages)
        self.content = rawData

    def output(self):
        print self.numberOfPages, " | "
        print self.numberOfPages, " | striped: ", self.striped, " | id:", self.id

    def flash(self):
        file = open(self.id, "w")
        file.write(self.content)
        file.close()

if __name__ == "__main__":
    print "starting..."
    ena = Page("http://www.ceid.upatras.gr/index.html","")
    ena.output()
    duo = Page("http://www.mozilla.com/en-US/firefox/central/","")
    duo.output()
    print "ending.."