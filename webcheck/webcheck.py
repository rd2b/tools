#!/usr/bin/env python

""" webcheck.py : Description """

__author__ = "R 2b"
__date__ = "2012/12/06"


import argparse
import urllib2

import cherrypy

class Checker():
    """ Checks if keywords are in given urls """

    def __init__(self ):
        self.urls = {}
        self.keywords = {}
        self.times = {}
        self.times["timeout"] = 120

    def add(self, url):
        if not self.urls.has_key(url):
            self.urls[url] = False

    def addkeyword(self, url, keyword):
        if not self.urls.has_key(url):
            self.add(url)
        self.keywords[url] = keyword

    def markavailable(self, url):
        self.urls[url] = True

    def markunavailable(self, url):
        self.urls[url] = False

    def __str__(self):
        urls = str(self.urls)
        keywords = str(self.keywords)
        return str((urls, keywords))

    def tohtml(self):
        message = self.report(html = True)
        print message
        return message

    def schedulenext(self):
        self.times["timeout"] = 120


    def report(self, html = False):
        response = "" 
        for url in self.urls.keys():
            message = ""
            if (self.urls[url] and self.keywords.has_key(url)):
                message = \
                        "{0} found with correct keyword '{1}'.".format(
                                url, self.keywords[url])
            elif (self.urls[url]):
                message = "{0} found.".format(url)
            else:
                message = "{0} not found.".format(url)
            response += message
            if html:
                response += "<br>"
        return response


    def runcheck(self, url):
        print "Checking " + url
        try:
            openned = urllib2.urlopen( url, timeout = 2 )
            if self.keywords.has_key(url):
                if self.keywords[url] in openned.read():
                    self.markavailable(url)
                else:
                    self.markunavailable(url)
            else:
                self.markavailable(url)
        except ValueError:
            print "Not a valid URL " + url
        except IOError:
            self.markunavailable(url)

    def check(self ):
        for url in self.urls.keys():
            self.runcheck(url)

class WebServer:
    def __init__(self, checker):
        self.checker = checker

    @cherrypy.expose
    def index(self, url = None, keyword = None):
        if( url and keyword ):
            self.checker.addkeyword(url, keyword)
            self.checker.runcheck(url)
        elif ( url ):
            self.checker.add(url)
            self.checker.runcheck(url)

        self.checker.check()

        formulaire = """
            <form action="index">
            <p>URL<p/><input type=text name="url"></input>
            <p>Keyword<p/><input type=text name="keyword"></input>
            <input type=submit>
            <form>"""

        response = "<div>{0}</div><div>{1}</div>".format(
                self.checker.tohtml(),formulaire)
        return response

def main():
    """ Default main function """
    # parse command line options
    parser = argparse.ArgumentParser(description="Checks if urls are fine")
    parser.add_argument(
        '-u', '--url', 
        type=str, default=[], action='append', help='Url to check')
    parser.add_argument(
        '-U', '--urls', type=str, default=[], help='Url to check' )
    args = parser.parse_args()

    checker = Checker()

    for url in args.url + args.urls.split():
        arr = url.split(",")
        checker.add(arr[0])
        if (len(arr) == 2):
            checker.addkeyword(arr[0], arr[1])

    cherrypy.quickstart(WebServer(checker))



if __name__ == "__main__":
    main()


