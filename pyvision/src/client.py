#!/usr/bin/env python
#########################################################
#	Name: 	client.py				#
#	Description: TODO				#
#########################################################


from ZSI import ServiceProxy
import ComplexTypes

import sys
import logging
import argparse
import ConfigParser

from datetime import datetime, timedelta

MESSAGE = "Hello from Python!"
DEFAULTCONFIGFILE="./configfile"

def readCommandFile(path=""):
    if not path:
        return None
    parser = ConfigParser.ConfigParser()
    parser.read(path)
    section = "Command"
    if not parser.has_section(section):
        return None
    c = Control()
    starting = parser.get(section,"starting")
    seconds = parser.get(section,"seconds")
    import re
    c.starting=(re.match("[\d|/\|:|\s]+",starting))
    c.seconds=(re.match("\number+",seconds))

    c.command = parser.get(section,"command")


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info("Starting...")

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configfile", dest="configfile", type=str)
    args = parser.parse_args()

    if not args.configfile : 
        args.configfile = DEFAULTCONFIGFILE
    configparser = ConfigParser.ConfigParser()
    configparser.read('args.configfile')


    logging.info("Using Config file = %s", str(args.configfile)) 

    nsdict = { 'types' : 'http://pycon.org/typs' }
    server = ServiceProxy.ServiceProxy( './wsdl/binding.wsdl')

    print ' Sending: %s' % MESSAGE
    response = server.echo(Message = MESSAGE)
    print 'Response: %s' % response['Message']
    one=1
    two=2
    response = server.add(One=one,Two=two)
    print 'Response: %s' % response['Result']
    response = server.send( Date = '2011/12/17',
                            Sender = 'tekos@test.net',
                            Reference = 'disk',
                            Host = "ref01.prod.test.net",
                            Message = 'Free space on /var/log < 20% ',
                            Priority = 0)
    print response
    response = server.getalerts(Message = "Gimme")
    print response


if __name__ == '__main__':
    main()
