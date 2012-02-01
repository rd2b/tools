#!/usr/bin/env python
#########################################################
#	Name: 	client.py				#
#	Description: TODO				#
#########################################################


from ZSI import ServiceProxy
from ComplexTypes import Control, Alert

import sys
import logging
import argparse
import ConfigParser

from datetime import datetime, timedelta
import time
from collections import deque

MESSAGE = "Hello from Python!"
DEFAULTCONFIGFILE = "/etc/pyvision/configfile"

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
            command = Control(path=myfile)
            if command :
                commands.append(command)
        else :
            logging.info("%s is not a valid configfile"% myfile)

    logging.debug("Ordering list for execution")
    logging.debug("Before :%s"% commands)
    commands.sort()
    logging.debug("After :%s"% commands)
    
    return commands
    
def execute(control):
    if not control: 
        return None
    command = control.command
    if not command:
        return None
    
    import shlex, subprocess
    args = shlex.split(command)
    logging.info("Excuting %s:"%command)
    logging.debug("Arguments %s:"%args)
    p = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    returncode = p.wait()
    output = p.stdout.read() + p.stderr.read()
    logging.info("Result : %s"%output)
    return (output, returncode)
    
def convertToAlert(control, result):
    if not control or not result:
        return none
    alert = Alert(date = str(datetime.now()),
          sender = "",
          reference = "",
          host = "",
          message = result[0],
          priority = result[1])
    return alert

def send(alert):
    if not alert:
         return None
    nsdict = { 'types' : 'http://pycon.org/typs' }
    server = ServiceProxy.ServiceProxy( './wsdl/binding.wsdl')
    response = server.send( Date = alert.date,
                            Sender = alert.sender,
                            Reference = alert.reference,
                            Host = alert.host,
                            Message = alert.message,
                            Priority = alert.priority)
    logging.info("Got response : %s"% response)

def run(mycontrols = None):
    def runControl(myc = None):
        logging.info("Initializing new control: %s"%myc)
        if not myc:
            return None
        logging.info("Initializing new control: %s"%myc)
        while True:
           schd = myc.schedule()
           dt = schd - datetime.now()
           time.sleep(dt.total_seconds())
           logging.info("Executing new control: %s"%myc)
           result = execute(myc)
           logging.debug("Result = '%s', Code = '%s' "%(result[0],result[1]))
           send(convertToAlert(control = myc, result = result))
           
   
    from multiprocessing import Process
    for c in mycontrols:
        p = Process(target=runControl, args=(c,))
        p.start()


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

    run(getCommands(commandsdir, extension))
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
