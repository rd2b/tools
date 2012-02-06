#!/usr/bin/env  python
#########################################################
#	Name:  	Worker.py				#
#	Description:  Action worker			#
#########################################################
#  -*- coding: UTF-8 -*-

from  ComplexTypes import Alert
from  dbhandler import DbHandler

class  Worker(object):
    """ Interacts with database"""
    mydb = None

    def __init__(self):
        self.mydb = DbHandler()
        self.mydb.createengine(url = 'sqlite:///:memory:')

    def registeralert(self, alert = None):
        if alert is None :
            return False
        session = self.mydb.getsession()
        session.add(alert)
        session.commit()
        return True

    def  getalerts(self):
        alerts = self.mydb.getsession().query(Alert)
        return alerts

