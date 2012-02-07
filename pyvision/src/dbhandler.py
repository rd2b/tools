#!/usr/bin/env python
#########################################################
#	Name: 	dbhandler.py				#
#	Description: Handles database objects		#
#########################################################
# -*- coding: UTF-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Sequence
from sqlalchemy import MetaData
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

from ComplexTypes import Alert

METADATA = MetaData()

ALERTS_TABLE = Table('alerts', METADATA,
    Column('id', Integer, Sequence('alert_id_seq'), primary_key=True),
    Column('sender', String(100)),
    Column('reference', String(100)),
    Column('host', String(255)),
    Column('message', String(255)),
    Column('date', String(20)),
    Column('priority', Integer)
)

mapper(Alert, ALERTS_TABLE) 

class DbHandler(object):
    """
Handles a Database object
Example :
alert = Alert()
dbhandler = DbHandler()
dbhandler.createengine(url = 'sqlite:///:memory:')
session = dbhandler.createsession()
try:
    session.add(alert)
    myalert = dbhandler.getsession().query(Alert).first() 
    dbhandler.getsession().commit()
    print myalert
except Exception as exc:
    print exc
   """
    engine = None
    session = None
    def __init__(self):
        pass

    def createengine(self, url):
        self.engine = create_engine(url, echo = True)
        METADATA.create_all(self.engine)

    def createsession(self):
        if self.engine != None :
            mysessionmaker = sessionmaker(bind = self.engine)
            self.session = mysessionmaker()
            return self.session

    def getsession(self):
        if not self.session :
            self.createsession()
        return self.session

    def commit(self):
        self.session.commit()

##Exemples :

