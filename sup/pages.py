#!/usr/bin/env python

""" pages.py : Description """

import webapp2
import logging

from worker import Storage


class WebServer:
    _storage = Storage()

    def storage(self, storage = None ):
        if storage:
            self._storage = storage
        return self._storage


class Overview(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(str(ws.storage()))

class Event(webapp2.RequestHandler):
    def get(self):
        timestamp = self.request.get('timestamp') 
        reference = self.request.get('reference')
        level = self.request.get('level')
        test = self.request.get('test')
        data = self.request.get('data')

        logging.info("Registering {0}, {1}, {2}, {3} {4}".format(
            str(timestamp), reference, level, test, data))

        try:
            ws.storage().append(
                timestamp = timestamp,
                reference = reference,
                level = level,
                test = test,
                data = data)

            response = "Success"
        except ValueError:
            logging.error("Supplied an invalid input")
            response = "Failed"

        self.response.write(response)


ws = WebServer()

app = webapp2.WSGIApplication([
    ('/', Overview),
    ('/overview', Overview),
    ('/event', Event)], debug=True)                    
  
