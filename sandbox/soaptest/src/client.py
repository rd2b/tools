#!/usr/bin/env python

from ZSI import ServiceProxy
import sys

MESSAGE = "Hello from Python!"

def main():
    server = ServiceProxy.ServiceProxy('../wsdl/binding.wsdl', use_wsdl=True)

    print ' Sending: %s' % MESSAGE
    response = server.echo(Message=MESSAGE)
    print 'Response: %s' % response['Message']
    response = server.add(one=1)
    print 'Response: %s' % response['result']


if __name__ == '__main__':
    main()
