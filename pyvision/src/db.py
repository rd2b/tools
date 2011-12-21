#!/usr/bin/env python
#########################################################
#	Name: 	db.py		#
#	Description: TODO	#
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

metadata = MetaData()

alerts_table = Table('alerts', metadata,
   Column('id', Integer, Sequence('alert_id_seq'), primary_key=True),
   Column('sender', String(100)),
   Column('reference', String(100)),
   Column('message', String(255)),
   Column('date', String(20)),
   Column('priority', Integer)
)

mapper(Alert, alerts_table) 

class Db(object):
    engine = None
    session = None
    def __init__(self):
         pass

    def create_engine(self, url):
        self.engine = create_engine(url, echo=True)
        metadata.create_all(self.engine)

    def create_session(self):
        if self.engine != None :
            Session = sessionmaker()
            Session.configure(bind=self.engine)
            self.session = Session()

    def getSession(self):
        return self.session

    def commit(self):
        return self.session.commit()

##Exemples :
a = Alert()
db = Db()
db.create_engine('sqlite:///:memory:')
db.create_session()
db.getSession().add(a)
myalert = db.getSession().query(Alert).first() 
db.getSession().commit()
print myalert

