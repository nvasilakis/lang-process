"""Extract list of URLs in a web page

This library is used to extract URLs from web pages. It is part of the language
processing project and directly used in the crawler class
"""
# from sgmllib import SGMLParser
from HTMLParser import HTMLParser

class Parser(HTMLParser):
	def reset(self):
		HTMLParser.reset(self)
		self.made = []
		self.urls = []
		self.text = []

	# Defining a number of filters in order to check if a link is valid
	# for addition in the URL queue
	def start_a(self, attrs):
		href = ["%s" % v  for k, v in attrs if k=='href' and
				'mailto' not in v and
				'.com' in v and 'acm.org' not in v and
				'wikipedia' not in v and '.gov' not in v and
				'.pdf' not in v and '.doc' not in v and
				'.xls' not in v and '.php' not in v and
				'.cgi' not in v and '.ics' not in v and
				'.js' not in v
		]
		if href:
			if "ics" in href:
				print "===>", href
			self.urls.extend(href)

	def start_link(self, attrs):
		href = ["%s ++ %s" % (k,v) for k, v in attrs if k=='href']
		if href:
			self.made.extend(href)

	def handle_starttag(self, tag, attrs):
		#attrs = dict(attrs)
		if tag.lower() == 'a':
			href = ["%s" % v  for k, v in attrs if k=='href' and
				'mailto' not in v and
				'.com' in v and 'acm.org' not in v and
				'wikipedia' not in v and '.gov' not in v and
				'.pdf' not in v and '.doc' not in v and
				'.xls' not in v and '.php' not in v and
				'.cgi' not in v and '.js' not in v
			]
			if href:
#				print "===>", href
				self.urls.extend(href)

	def handle_data(self, text):
		self.text.extend(text)
