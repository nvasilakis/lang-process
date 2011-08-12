"""A Web Page class implementing single-page stats and functions.


"""

import re
from lxml.html import clean
import nltk

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
		# TODO: TEST SMALL FILE NAMES!!
		transform = "|".join(self.striped.split("/"))
		transform = (transform[-1]=="|") and transform[:-2] or transform
		transform=  transform.__len__() > 10 and transform[4:5+4] + transform[-5:] or transform
		self.id = transform + "--" + str(self.__class__.numberOfPages)
		self.raw = rawData
		self.tokenized = []

	def output(self):
		print self.numberOfPages, " | striped: ", self.striped, " | id:", self.id

	def flash_HTM(self):
		print "flashing ", self.url
		file = open("local/" + self.id + ".html", "w") #Adding a .html extension for easiness
		file.write(self.raw)
		file.close()

	def flash_TKN(self,mode):
		self.tokenize(mode)
		file = open("local/" + self.id + ".tkn", "w") #Adding a .tkn extension for consistency
		file.write("".join(self.tokenized))
		file.close()

	def	flash(self):
		#filetypes = ["htm","tkn"]
		#[getattr(self,"flash_"+f.upper()) for f in filetypes]
		self.flash_HTM()
		self.flash_TKN("max")

	def tokenize(self, granularity="max"): # use granularity to debug!
		"""
		It extracts actual text from wep pages.

		Implements three granularity levels (min, med, max):
		 * min represents text in the style of an one-line string
		 * med represents text in the style closest to the format of a web page
		 * max represents text in word tokens
		"""
		strippedJS = clean.clean_html(self.raw)
		strippedHTML = nltk.util.clean_html(strippedJS)
		ampersands = "&[a-zA-Z]{2,4};"					# remove html ampersand commands
		stripped = re.sub(ampersands,"",strippedHTML) 	# such as &amp; &gt; etc
		tokensFormat = (granularity=="med") and (lambda l: l) or (lambda l: "\n".join(l.split()))
		self.tokenized = tokensFormat(stripped)
		

if __name__ == "__main__":
	print "starting..."
	ena = Page("http://www.ceid.upatras.gr/index.html","Hello1")
	ena.output()
	ena.flash()
	duo = Page("http://www.mozilla.com/en-US/firefox/central/","Hello2")
	duo.output()
	duo.flash()
	print "ending.."