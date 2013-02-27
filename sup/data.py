#!/usr/bin/env python

""" data.py : Description """

__author__ = "<author>"
__date__ = "2013/01/31"


class Data:
    _level = 0
    _test = "default"
    _reference = ""
    _timestamp = 0
    _level = 0
    _data = ""

    def __init__(self, timestamp, reference, level, test, data):
        self.timestamp(timestamp)
        self.reference(reference)
        self.level(level)
        self.test(test)
        self.data(data)

    def timestamp(self, timestamp = None):
        if timestamp:
            self_timestamp = timestamp
        return self._timestamp

    def reference(self, reference = None):
        if reference:
            self._reference = reference
        return self._reference

    def level(self, level = None):
        if level:
            self._level = level
        return self._level

    def test(self, test = None):
        if test:
            self._test = test
        return self._test

    def data(self, data = None):
        if data:
            self._data = data
        return self._data


    def __str__(self):
        return str({
            "timestamp" : self.timestamp(),
            "reference" : self.reference(),
            "test" : self.test(),
            "level" : self.level(),
            "data" : self.data()})

