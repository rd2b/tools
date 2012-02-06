#!/usr/bin/env python
#########################################################
#	Name: 	Worker.py		#
#	Description: TODO	#
#########################################################
# -*- coding: UTF-8 -*-

from ComplexTypes import Alert
from dbhandler import DbHandler

class g:
    mydb = None

def init():
    g.mydb = DbHandler()
    g.mydb.createengine('sqlite:///:memory:')
    g.mydb.createsession()

def registeralert(alert = None):
    if alert is None :
        return False
    print alert
    g.mydb = DbHandler()
    g.mydb.createengine('sqlite:///:memory:')
    session = g.mydb.createsession()
    print alert
    session.add(alert)
    session.commit()
    return True

def getalerts(message = None):
    g.mydb.createsession()
    alerts = g.mydb.getsession().query(Alert)
    return alerts

def registeralert(alert = None):
    if alert is None :
        return False
    try :
        g.mydb.createsession()
        g.mydb.getsession().add(alert)
        g.mydb.getsession().commit()
        myalert = g.mydb.getsession().query(Alert).first()
        print myalert.date
        return True
    except :
        raise

