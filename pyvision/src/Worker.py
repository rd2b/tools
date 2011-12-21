#!/usr/bin/env python
#########################################################
#	Name: 	Worker.py		#
#	Description: TODO	#
#########################################################
# -*- coding: UTF-8 -*-

from ComplexTypes import Alert
from db import Db

def registeralert(alert = None):
    if alert = None :
        return False
    g.mydb.create_session()
    g.mydb.getSession().add(a)
    g.mydb.getSession().commit()
    myalert = g.mydb.getSession().query(Alert).first()
    print myalert.date
    response._Message = "OK"
    return response

