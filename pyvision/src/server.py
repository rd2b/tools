#!/usr/bin/env python

import logging

from ZSI import dispatch
from PyVision_server import EchoResponse
from PyVision_server import AddResponse
from PyVision_server import SendResponse
from PyVision_server import GetAlertsResponse

from ComplexTypes import Alert
from db import Db

import Worker

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
    logging.info( "My alert is : " + str(alert))
    a = Alert( date = alert['Date'],
               sender = alert['Sender'],
               reference = alert['Reference'],
               host = alert['Host'],
               message = alert['Message'],
               priority = alert['Priority'])
    if Worker.registeralert(a) :
        response._Message = "OK"
    else:
        response._Message = "KO"
    print response._Message
    return response

def getalerts(Message = None):
    logging.debug("Asking for alerts.")
    response=GetAlertsResponse()
    alerts = Worker.getalerts()
    response._Message = ""
    for a in alerts:
        response._Message += str(a) + "\n"
    logging.debug("Sending alerts : " + response._Message)
    return response
    

def main():
    logging.info("Starting...")
    Worker.init()
    dispatch.AsServer(port=8080)
    logging.info("Exiting...")

if __name__ == '__main__':
    main()
