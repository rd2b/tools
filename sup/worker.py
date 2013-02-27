#!/usr/bin/env python

""" worker.py : Description """

__author__ = "<author>"
__date__ = "2013/01/31"


import threading
class Storage:
    _tostore = []
    def __init__(self):
        pass

    def store(self, data):
        self._tostore.append(data)



