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
        self.raw = rawData
        self.tokenized = []

    def output(self):
        print self.numberOfPages, " | striped: ", self.striped, " | id:", self.id

    def flash(self):
        print "flashing ", self.url
        file = open("local/" + self.id + ".html", "w") #Adding a .html extension for easiness
        file.write(self.raw)
        file.close()

    def flashTkn(self):
        file = open("local/" + self.id + ".tkn", "w") #Adding a .tkn extension for consistency
        data1 = "".join(self.tokenized)
        data2 = data1.split()
        data = "\n".join(data2)
        #data = [d for d in data if d!=""]
        #introduce re!
        file.write("".join(data1))
        file.close()

    def tokenize(self):
        pass

if __name__ == "__main__":
    print "starting..."
    ena = Page("http://www.ceid.upatras.gr/index.html","Hello1")
    ena.output()
    ena.flash()
    duo = Page("http://www.mozilla.com/en-US/firefox/central/","Hello2")
    duo.output()
    duo.flash()
    print "ending.."