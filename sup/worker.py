#!/usr/bin/env python

""" worker.py : Description """

__author__ = "Remi Debay"
__date__ = "2013/01/31"


import threading
class Storage:
    _datas = {}

    def __init__(self):
        pass

    def append(self, data):
        datas = self.datas()
        if  not data.reference in datas :
            datas[data.reference] = {}

        if not data.test in datas[data.reference]:
            datas[data.reference][data.test] = {}

        datas[data.reference][data.test][data.timestamp] = data

        
    def datas(self):
        return self._datas


    def __str__(self):
        response = []
        datas = self.datas()
        for byreference in datas.values():
            for bytest in byreference.values():
                for bytime in bytest.values():
                    response.append(str(bytime))
        return str(response)
