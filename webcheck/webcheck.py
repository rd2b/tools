#!/usr/bin/python

""" webcheck.py : Description """

__author__ = "R 2b"
__date__ = "2012/12/06"

import argparse
import urllib2

import logging


import cherrypy

from threading import Thread
from Queue import Queue

class UrlCheck():
    def __init__(self, url, timeout = 2):
        self.url = url
        self.timeout = timeout
        self.keywords = dict()
        self.available = False

    def addkeyword(self, keyword):
        self.keywords[keyword] = False

    def finded(self, keyword):
        self.keywords[keyword] = True

    def missing(self, keyword):
        self.keywords[keyword] = False

    def __str__(self):
        return str({ 
            "url" : self.url, 
            "available" : str(self.available),
            "timeout" : str(self.timeout),
            "keywords" : str(self.keywords)
            })

    def markavailable(self):
        self.available = True

    def markunavailable(self):
        self.available = False

    def runcheck(self):
        logging.info("Checking {0}".format(self.url))
        try:
            openned = urllib2.urlopen( self.url, timeout = self.timeout )
            self.markavailable()
            content = openned.read()

            for keyword in self.keywords.keys():
                logging.info("Checking {0} with keyword {1}".format(
                    self.url, keyword))
                if keyword in content:
                    self.finded(keyword)
                else:
                    self.missing(keyword)
        except ValueError:
            logging.error("Not a valid URL %s.", url)
        except IOError:
            self.markunavailable()

    def repport (self):
        message = ""
        if self.available:
            message = "{0} available.".format(self.url)
        else:
            message = "{0} not available.".format(self.url)

        for keyword in self.keywords.keys():
            print(self.keywords)
            if self.keywords[keyword]:
                message += "{0} found with correct keyword '{1}'.".format(
                        self.url, keyword)
            else:
                message += "{0} has no keyword like '{1}'.".format(
                        self.url, keyword)
        return message
 



class Checker():
    """ Checks if keywords are in given urls """

    def __init__(self, workers = 5 ):
        self.urls = {}
        self.workers = []
        self.times = {}
        self.queue = Queue()

        for workerid in range(workers):
            newworker = Thread(target = self.worker)
            logging.debug("Thread %s started", workerid)
            newworker.daemon = True
            newworker.start()
            self.workers.append(newworker)

    def add(self, url):
        if ( url not in self.urls and not url == "" ):
            self.urls[url] = UrlCheck(url)

    def addkeyword(self, url, keyword):
        self.add(url)
        self.urls[url].addkeyword(keyword)

    def __str__(self):
        return str(self.urls)

    def tohtml(self):
        message = self.report(html = True)
        logging.debug(message)
        return message

    def schedulenext(self):
        self.times["timeout"] = 120

    def report(self, html = False):
        response = "" 
        for url in self.urls.keys():
            response += self.urls[url].repport()
            if html:
                response += "<br>"
        return response

    def check(self, url):
        if url in self.urls:
            self.queue.put(self.urls[url])

    def worker(self):
        while True:
            logging.debug("I am waiting for tasks.")
            checker = self.queue.get()
            logging.debug("I am working on task.")
            checker.runcheck()
            self.queue.task_done()

    def checkall(self ):
        logging.info("Starting check")

        for url in self.urls.values():
            logging.debug("Sending %s to task queue.", url)
            self.queue.put(url)

        if not ( len(self.urls) == 0 and self.queue.empty() ):
            self.queue.join()
        logging.info("Ending check")

class WebServer:
    def __init__(self, checker):
        self.checker = checker

    @cherrypy.expose
    def index(self, url = None, keyword = None):
        if url:
            self.checker.add(url)
            if keyword:
                self.checker.addkeyword(url, keyword)

            self.checker.check(url)

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
    myformat = "%(asctime)s %(message)s"
    logging.basicConfig(
            level = logging.INFO,
            format = myformat)

    logging.info("Program starting...")

    # parse command line options
    parser = argparse.ArgumentParser(description="Checks if urls are fine")
    parser.add_argument(
        '-u', '--url', 
        type=str, default='', action='append', help='Url to check')
    parser.add_argument(
        '-U', '--urls', type=str, default="", help='Url to check' )
    args = parser.parse_args()

    checker = Checker()
     
    urls = []
    urls.append(args.url)
    urls.extend(args.urls.split())

    for url in urls:
        arr = url.split(",")
        checker.add(arr[0])
        if (len(arr) == 2):
            checker.addkeyword(arr[0], arr[1])

    checker.checkall()
    cherrypy.quickstart(WebServer(checker))



if __name__ == "__main__":
    main()


