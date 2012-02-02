#!/usr/bin/env python
#########################################################
#	Name: 	client.py				#
#	Description: client used to check 		#
#			and send acontrols		#
#########################################################


from ZSI import ServiceProxy
from ComplexTypes import Control, Alert

import time
import logging
import argparse
import ConfigParser
import shlex
import os
import subprocess

from datetime import datetime 
from multiprocessing import Process

MESSAGE = "Hello from Python!"
DEFAULTCONFIGFILE = "/etc/pyvision/configfile"

def getcommands(path=None, extension=".pv"):
    if not path or not os.path.isdir(path):
        return None
    entries = os.listdir(path)
    logging.debug("Entries in "+ path +","+ str(entries))
    commands = []
    for entry in entries:
        myfile = path + os.sep + entry
        if os.path.splitext(myfile)[1] == extension :
            command = Control(path = myfile)
            if command :
                commands.append(command)
        else :
            logging.info(str(myfile) + " is not a valid configfile")

    logging.debug("Ordering list for execution")
    logging.debug("Before :"+ str(commands))
    commands.sort()
    logging.debug("After :"+ str(commands))
    
    return commands
    
def execute(control):
    if not control: 
        return None
    command = control.command
    if not command:
        return None
    
    args = shlex.split(command)
    logging.info("Excuting "+ command)
    logging.debug("Arguments "+ str(args))
    process = subprocess.Popen(args, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE)
    returncode = process.wait()
    output = process.stdout.read() + process.stderr.read()
    logging.info("Result : "+str(output))
    return (output, returncode)
    
def converttoalert(control, result):
    if not control or not result:
        return None
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
    server = ServiceProxy.ServiceProxy( './wsdl/binding.wsdl')
    response = server.send( Date = alert.date,
                            Sender = alert.sender,
                            Reference = alert.reference,
                            Host = alert.host,
                            Message = alert.message,
                            Priority = alert.priority)
    logging.info("Got response : "+ str( response))

def run(mycontrols = None):
    def runcontrol(myc = None):
        logging.info("Initializing new control: "+ str(myc))
        if not myc:
            return None
        logging.info("Initializing new control: "+ str(myc))
        while True:
            schd = myc.schedule()
            delta = schd - datetime.now()
            time.sleep(delta.total_seconds())
            logging.info("Executing new control: "+ str(myc))
            result = execute(myc)
            logging.debug("Result = '"+str(result[0])+
                          "', Code = '"+str(result[1])+"'")
            send(converttoalert(control = myc, result = result))
           
   
    for control in mycontrols:
        process = Process(target=runcontrol, args=(control,))
        process.start()


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
    logging.info("Using configfile " + str(configfile))

    try:
        section = "PyVision"
        configparser = ConfigParser.ConfigParser()
        configparser.read(configfile)
        logging.debug(str(configparser.sections()))
        commandsdir = configparser.get(section, "commandsdir")
        extension = configparser.get(section, "extension")
    except ConfigParser.NoSectionError as nse:
        logging.error(nse)
        return 401
    logging.info("Using commands files in %s with exetnsion %s" \
			% (commandsdir, extension))

    run(getcommands(commandsdir, extension))

#
#    print ' Sending: %s' % MESSAGE
#    response = server.echo(Message = MESSAGE)
#    print 'Response: %s' % response['Message']
#    one=1
#    two=2
#    response = server.add(One=one,Two=two)
#    print 'Response: %s' % response['Result']
#    response = server.send( Date = '2011/12/17',
#                            Sender = 'tekos@test.net',
#                            Reference = 'disk',
#                            Host = "ref01.prod.test.net",
#                            Message = 'Free space on /var/log < 20% ',
#                            Priority = 0)
#    print response
#    response = server.getalerts(Message = "Gimme")
#    print response


if __name__ == '__main__':
    main()
