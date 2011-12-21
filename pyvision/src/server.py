#!/usr/bin/env python

from ZSI import dispatch
from PyVision_server import EchoResponse
from PyVision_server import AddResponse
from PyVision_server import SendResponse

from ComplexTypes import Alert
from db import Db

class g:
    mydb = None

def echo(message):
    response = EchoResponse()
    response._Message = message
    return response

def add( operators ):
    response = AddResponse()
    print operators
    response._Result = 0
    for o in operators:
        op = operators[o]
        response._Result += op
    return response

def send( alert ):
    response = SendResponse()
    print alert
    a = Alert( date = alert['Date'],
               sender = alert['Sender'],
               reference = alert['Reference'],
               message = alert['Message'],
               priority = alert['Priority'])
    g.mydb.create_session()
    g.mydb.getSession().add(a)
    g.mydb.getSession().commit()
    myalert = g.mydb.getSession().query(Alert).first()
    print myalert.date
    response._Message = "OK"
    return response

def main():
    g.mydb = Db()
    g.mydb.create_engine('sqlite:///:memory:')
    g.mydb.create_session()
    dispatch.AsServer(port=8080)#, typesmodule=(ComplexTypes,))

if __name__ == '__main__':
    main()
