#!/usr/bin/env python

from ZSI import ServiceProxy
import ComplexTypes

import sys

MESSAGE = "Hello from Python!"

def main():
    nsdict = { 'types' : 'http://pycon.org/typs' }
    server = ServiceProxy.ServiceProxy( './wsdl/binding.wsdl')

    print ' Sending: %s' % MESSAGE
    response = server.echo(Message=MESSAGE)
    print 'Response: %s' % response['Message']
    one=1
    two=2
    response = server.add(One=one,Two=two)
    print 'Response: %s' % response['Result']
    response = server.send( Date='2011/12/17',
                            Sender='mysender',
                            Reference = 'reference',
                            Message = 'message',
                            Priority =0)
    print response


if __name__ == '__main__':
    main()
