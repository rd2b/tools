
from datetime import datetime, timedelta

import logging
import re
import ConfigParser

class Alert(object):
    id = None
    def __init__(self, date=None, 
                       sender=None, 
                       reference=None, 
                       host=None,
                       message=None,
                       priority=0):
        self.date = date
        self.sender = sender
        self.reference = reference
        self.host = host
        self.message = message
        self.priority = priority

    def __repr__(self):
        return "<Alert('%s','%s', '%s', '%s','%s','%s')>" % (self.date,
               self.sender, self.reference, self.host, 
               self.message, str(self.priority))

class Control(object):
    _next = None
    _commandsection = "Command"

    def __init__(self, starting = datetime.now(), 
                       seconds = 0,
                       reference = "defaultreference", 
                       command = ""):
        self.starting = starting
        self.seconds = seconds
        self.reference = reference
        self.command = command

    def __init__(self, path=""):
        logging.debug("Reading path "+ path)
        if not path:
            logging.warn("Invalid path %s" % path)
            return None
        parser = ConfigParser.ConfigParser()
        parser.read(path)
        if not parser.has_section(self._commandsection):
            logging.warn("Section "+ self._commandsection +
                            " not found in "+ path)
            return None
        starting = parser.get(self._commandsection, "starting")
        seconds = parser.get(self._commandsection, "seconds")
        command = parser.get(self._commandsection, "command")
        if parser.has_option(self._commandsection, "reference"):
            reference = str(parser.get(self._commandsection, "reference"))
            self.setreference(reference)
        else :
            self.setreference("default")
        logging.debug("starting "+ starting +", seconds, "+ seconds)

        self.setstarting(starting)
        self.setseconds(seconds)
        self.setcommand(command)

        logging.debug("Found Control:%s" % self)

    def setstarting(self, starting):
        try:
            if starting and starting != "" :
                self.starting = datetime.strptime(starting, "%Y-%m-%d %H:%M")
            else:
                self.starting = None
        except ValueError as err:
            logging.warn(err)
            self.starting = None

    def setseconds(self, seconds):
        matched = re.match('(\d+)', str(seconds))
        if matched:
            self.seconds = int(matched.group(1))
        else:
            self.seconds = 0

    def setreference(self, reference):
        self.reference = reference

    def setcommand(self, command):
        self.command = command

    def __gt__(self, other):
        myschedule = self.schedule()
        otherschedule = other.schedule()
        return myschedule > otherschedule

    def __eq__(self, other):
        myschedule = self.schedule()
        otherschedule = other.schedule()
        return myschedule == otherschedule

    def __lt__(self, other):
        myschedule = self.schedule()
        otherschedule = other.schedule()
        return myschedule < otherschedule
    
    def __repr__(self):
        return "<Control('%s', '%s', '%s', '%s')>" % (self.starting,
                        self.seconds, self.reference, self.command)

    def schedule(self):
        """
            Return next scheduling for Control
            Return None if Control should not be schedule
        """
        now = datetime.now()
        if self._next and self._next > now:
            return self._next
        now = datetime.now()
        if  self.seconds < 0 or ( self.seconds == 0 \
		and ( not self.starting or self.starting < now )):
            self._next = None
            return None 
        elif not self.starting:
            self.starting = now

        nextexecution = self.starting
        if self.seconds and self.seconds > 0 :
            delta = now - nextexecution
            multi = delta.total_seconds() // self.seconds
            logging.debug("Total:"+str(delta.total_seconds())+
                             " multi:"+ str(multi) +
                             " seconds:"+ str(self.seconds))
            delta = timedelta(seconds = self.seconds * multi + self.seconds)
            nextexecution = nextexecution + delta

            delta = timedelta(seconds = self.seconds )
            while nextexecution < now and delta:
                nextexecution = nextexecution + delta
        logging.debug("Next execution %s for %s"%(nextexecution, self._next))
        self._next = nextexecution
        return nextexecution

