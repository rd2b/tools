#!/usr/bin/env python

from ZSI import dispatch
from Test_server import EchoResponse
from Test_server import AddResponse

def echo(message):
    response = EchoResponse()
    response._Message = message
    return response

def add( one ):
    response = AddResponse()
    print one
    response._Result = one
    return response

if __name__ == '__main__':
    dispatch.AsServer(port=8080)
