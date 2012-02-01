
from datetime import datetime, timedelta

import logging

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
        import re
        import ConfigParser
        logging.debug("Reading path "+ path)
        if not path:
            logging.warn("Invalid path %s" % path)
            return None
        parser = ConfigParser.ConfigParser()
        parser.read(path)
        if not parser.has_section(self._commandsection):
            logging.warn("Section %s not found in %s"%
                            (self._commandsection,path))
            return None
        starting = parser.get(self._commandsection,"starting")
        seconds = parser.get(self._commandsection,"seconds")
        if parser.has_option(self._commandsection,"reference"):
            self.reference = str(parser.get(self._commandsection,"reference"))
        else :
            self.reference = "default"
        logging.debug("starting %s, seconds, %s"%(starting,seconds))
        try:
            if starting and starting != "" :
                self.starting = datetime.strptime(starting,"%Y-%m-%d %H:%M")
            else:
                self.starting = None
        except ValueError as err:
            logging.warn(err)

        m = re.match('(\d+)',str(seconds))
        if m:
             self.seconds = int(m.group(1))
        else:
            self.seconds = 0

        self.command = parser.get(self._commandsection,"command")
        logging.debug("Found Control:%s" % self)

    def __gt__(self, other):
       me = self.schedule()
       y = other.schedule()
       return me > y

    def __eq__(self,other):
       me = self.schedule()
       y = other.schedule()
       return me == y

    def __lt__(self, other):
       me = self.schedule()
       y = other.schedule()
       return me < y
    
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
             dt = now - nextexecution
             multi = dt.total_seconds() // self.seconds
             logging.debug("Total:%s multi:%s seconds:%s" 
		%(dt.total_seconds(), multi, self.seconds))
             delta = timedelta(seconds = self.seconds * multi + self.seconds)
             nextexecution = nextexecution + delta

             delta = timedelta(seconds = self.seconds )
             while nextexecution < now and delta:
                 nextexecution = nextexecution + delta
        logging.debug("Next execution %s for %s"%(nextexecution,self._next))
        self._next = nextexecution
        return nextexecution

