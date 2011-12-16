#!/usr/bin/env python

from ZSI import ServiceProxy
import sys

MESSAGE = "Hello from Python!"

def main():
    server = ServiceProxy.ServiceProxy('../wsdl/binding.wsdl', use_wsdl=True)

    print ' Sending: %s' % MESSAGE
    response = server.echo(Message=MESSAGE)
    print 'Response: %s' % response['Message']
    one=1
    two=2
    response = server.add(One=one,Two=two)
    #response = server.add(One=one)
    print 'Response: %s' % response['Result']


if __name__ == '__main__':
    main()
