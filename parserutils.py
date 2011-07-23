"""Extract list of URLs in a web page

This library is used to extract URLs from web pages. It is part of the language
processing project and directly used in the crowler class
"""
from sgmllib import SGMLParser

class Parser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.made = []
		self.urls = []

    # What you may not have realized before is that getattr will find
    # methods defined in descendants of an object as well as the object
    # itself.
	def start_a(self, attrs):
		href = ["%s" % v  for k, v in attrs if k=='href' and
                'mailto' not in v and
                '.com' in v and 'acm.org' not in v and
                'wikipedia' not in v and '.gov' not in v
        ]
		if href:
			self.urls.extend(href)

	def start_link(self, attrs):
		href = ["%s ++ %s" % (k,v) for k, v in attrs if k=='href']
		if href:
			self.made.extend(href)
