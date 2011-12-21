#!/usr/bin/env python

from ZSI import dispatch
from PyVision_server import EchoResponse
from PyVision_server import AddResponse
from PyVision_server import SendResponse

import ComplexTypes


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
    a = ComplexTypes.Alert( date = alert['Date'],
               sender = alert['Sender'],
               reference = alert['Reference'],
               message = alert['Message'],
               priority = alert['Priority'])
    print a
    print "OK"
    response._Message = "OK"
    return response

if __name__ == '__main__':
    dispatch.AsServer(port=8080, typesmodule=(ComplexTypes,))
