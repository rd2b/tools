#!/usr/bin/env python3

""" pages.py : Description """

import cherrypy
import logging

from data import Data
from worker import Storage

class WebServer:
    _storage = Storage()

    def __init__(self):
        pass

    def storage(self, storage = None ):
        if storage:
            self._storage = storage
        return self._storage


    @cherrypy.expose
    def all(self):
        response = str(self.storage())

        return response

    @cherrypy.expose
    def register(self, 
            timestamp, reference, level = 0, test = 'default', data = ""):

        logging.info("Registering {0}, {1}, {2}, {3} {4}".format(
            str(timestamp), reference, level, test, data))

        try:
            newdata = Data(timestamp = timestamp,
                reference = reference,
                level = level,
                test = test,
                data = data)
            self.storage().append(newdata)
            response = "Success"
        except ValueError:
            logging.error("Supplied an invalid input")
            response = "Failed"

        return response




