#!/usr/bin/env python
#########################################################
#	Name: 	client.py				#
#	Description: TODO				#
#########################################################


from ZSI import ServiceProxy
from ComplexTypes import Control

import sys
import logging
import argparse
import ConfigParser

from datetime import datetime, timedelta
from collections import deque

MESSAGE = "Hello from Python!"
DEFAULTCONFIGFILE="/etc/pyvision/configfile"

def readCommandFile(path=""):
    logging.debug("Reading path "+ path)
    if not path:
        logging.warn("Invalid path %s" % path)
        return None
    parser = ConfigParser.ConfigParser()
    parser.read(path)
    section = "Command"
    if not parser.has_section(section):
        logging.warn("Section %s not found in %s"%(section,path))
        return None
    c = Control()
    starting = parser.get(section,"starting")
    seconds = parser.get(section,"seconds")
    import re
    logging.debug("starting %s, seconds, %s"%(starting,seconds))
    try:
        if starting and starting != "" :
            c.starting=datetime.strptime(starting,"%Y-%m-%d %H:%M")
    except ValueError as err:
        logging.warn(err)

    m = re.match('(\d+)',str(seconds)) 
    if m :
        c.seconds = int(m.group(1))

    c.command = parser.get(section,"command")
    logging.debug("Found Control:\n%s\n%s\n%s" % (c.starting,c.seconds,c.command))
    
    return c


def getCommands(path=None, extension=".pv"):
    import os
    if not path or not os.path.isdir(path):
        return None
    entries = os.listdir(path)
    logging.debug("Entries in %s:%s"%(path,entries))
    commands = []
    for e in entries:
        myfile = path + os.sep + e
        if os.path.splitext(myfile)[1] == extension :
            command = readCommandFile(path=myfile)
            if command :
                commands.append(command)
        else :
            logging.info("%s is not a valid configfile"% myfile)

    logging.debug("Ordering list for execution")
    print commands
    commands.sort()
    print commands
    
    return None
    
def orderCommands(mylist=None,control=None):
    if not mylist:
        mylist=list()
    if control:
        mylist.append(control)
        mylist.sort()
    return mylist

def main():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info("Starting...")

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configfile", dest="configfile", type=str)
    args = parser.parse_args()

    if not args.configfile:
        configfile = DEFAULTCONFIGFILE 
    else:
        configfile = args.configfile 
    logging.info("Using configfile %s"%configfile)

    try:
        section = "PyVision"
        configparser = ConfigParser.ConfigParser()
        configparser.read(configfile)
        logging.debug(str(configparser.sections()))
        commandsdir = configparser.get(section,"commandsdir")
        extension = configparser.get(section,"extension")
    except ConfigParser.NoSectionError as nse:
        logging.error(nse)
        return 401
    logging.info("Using commands files in %s with exetnsion %s" \
			% (commandsdir, extension))

    getCommands(commandsdir, extension)
    return 0

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
