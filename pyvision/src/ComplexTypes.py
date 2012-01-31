
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

    def __init__(self, starting = datetime.now(), 
                       seconds = 0, 
                       command = ""):
       self.starting = starting
       self.seconds = seconds
       self.command = command

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
        return "<Control('%s','%s', '%s')>" % (self.starting, self.seconds, self.command)

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

