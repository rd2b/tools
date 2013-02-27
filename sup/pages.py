#!/usr/bin/env python3

""" pages.py : Description """

import cherrypy
import logging

from data import Data
from worker import Storage

class WebServer:
    _storage = {}

    def __init__(self):
        pass

    @cherrypy.expose
    def index(self):
        return "index"

    @cherrypy.expose
    def register(self, timestamp, reference, level = 0, test = 'default'):

        logging.info("Registering {0}, {1}, {2}, {3}".format(
            str(timestamp), reference, level, test))

        try:
            newdata = Data(timestamp = timestamp,
                reference = reference,
                level = level,
                test = test)
            response = "Success"
        except ValueError:
            logging.error("Supplied an invalid input")
            response = "Failed"

        return response




