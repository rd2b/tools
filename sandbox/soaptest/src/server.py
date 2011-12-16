#!/usr/bin/env python

from ZSI import dispatch
from Test_server import EchoResponse
from Test_server import AddResponse

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

if __name__ == '__main__':
    dispatch.AsServer(port=8080)
