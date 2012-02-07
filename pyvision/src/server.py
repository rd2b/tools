#!/usr/bin/env python

import logging

from ZSI import dispatch
from PyVision_server import EchoResponse
from PyVision_server import AddResponse
from PyVision_server import SendResponse
from PyVision_server import GetAlertsResponse

from ComplexTypes import Alert

from Worker import Worker

def echo(message):
    response = EchoResponse()
    response._Message = message
    return response

def add( operators ):
    response = AddResponse()
    print operators
    response._Result = 0
    for operator in operators:
        response._Result += operators[operator]
    return response

def send( alert ):
    logging.info("My alert is : " + str(alert))
    alertobject = Alert( date = alert['Date'],
               sender = alert['Sender'],
               reference = alert['Reference'],
               host = alert['Host'],
               message = alert['Message'],
               priority = alert['Priority'])
    response = SendResponse()
    try:
        myworker = Worker()
        myworker.registeralert(alertobject)
        response._Message = "OK"
    except Exception as error:
        logging.warn("Got error while registering alert")
        logging.info(error)
        response._Message = "KO"
    return response

def getalerts(Message = None):
    logging.debug("Asking for alerts.")
    response = GetAlertsResponse()
    alerts = Worker.getalerts()
    response._Message = ""
    for alert in alerts:
        response._Message += str(alert) + "\n"
    logging.debug("Sending alerts : " + response._Message)
    return response
    

def main():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info("Starting...")
    dispatch.AsServer(port=8080)
    logging.info("Exiting...")

if __name__ == '__main__':
    main()

