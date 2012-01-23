#!/usr/bin/env python
#########################################################
#	Name: 	Worker.py		#
#	Description: TODO	#
#########################################################
# -*- coding: UTF-8 -*-

from ComplexTypes import Alert
from db import Db

class g:
    mydb = None

def init():
    g.mydb = Db()
    g.mydb.create_engine('sqlite:///:memory:')
    g.mydb.create_session()

def registeralert(alert = None):
    if alert is None :
        return False
    g.mydb.create_session()
    g.mydb.getSession().add(alert)
    g.mydb.getSession().commit()
    return True

def getalerts(message = None):
    g.mydb.create_session()
    alerts = g.mydb.getSession().query(Alert)
    return alerts

def registeralert(alert = None):
    if alert is None :
        return False
    try :
        g.mydb.create_session()
        g.mydb.getSession().add(alert)
        g.mydb.getSession().commit()
        myalert = g.mydb.getSession().query(Alert).first()
        print myalert.date
        return True
    except :
        raise

