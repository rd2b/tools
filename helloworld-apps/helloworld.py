#!/usr/bin/env python

""" helloworld.py : Description """

__author__ = "<author>"
__date__ = "2013/03/05"

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, webapp2 World!')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

