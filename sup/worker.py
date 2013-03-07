#!/usr/bin/env python

""" worker.py : Description """

__author__ = "Remi Debay"
__date__ = "2013/01/31"


import threading

from google.appengine.ext import db

class Data(db.Model):
    level = db.IntegerProperty()
    test = db.StringProperty()
    reference = db.StringProperty() 
    timestamp = db.IntegerProperty()
    data = db.StringProperty(multiline = True)

class Storage:
    def __init__(self):
        pass

    def append(self, level, test, reference, timestamp, data):
        newdata = Data()
        
        newdata.level = int(level)
        newdata.test = str(test)
        newdata.reference = str(reference)
        newdata.timestamp = int(timestamp)
        newdata.data = str(data)

        newdata.put()


        
    def datas(self):
        datas = db.GqlQuery("Select * FROM Data "
                "ORDER BY reference, test, timestamp")
        return datas

    def lastsdatas(self):
        datas = self.datas

        last = []
        for data in datas:
            if ( not last[data.test][data.reference] 
                    or data.timestamp > last[data.test][data.reference].timestamp):
                last[data.test][data.reference] = data
        return last





    def __str__(self):
        response = []
        datas = self.datas()
        for data in datas:
            response.append(str(data))
        return str(response)
