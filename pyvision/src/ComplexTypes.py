
from datetime import datetime, timedelta

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
    def __init__(self, starting = datetime.now(), 
                       seconds = 0, 
                       command = ""):
       self.starting = starting
       self.seconds = seconds
       self.command = command
    
    def schedule(self):
        """
            Return next scheduling for Control
            Return None if Control should not be schedule
        """
        now = datetime.now()
        if self.seconds < 0 or ( self.seconds == 0 \
		and ( not self.starting or self.starting < now )):
            return None 
        if not self.starting:
            self.starting = now
        nextexecution = self.starting
        if self.seconds and self.seconds > 0 :
             delta = timedelta(seconds = self.seconds)
             while nextexecution < now and delta:
                 nextexecution = nextexecution + delta
                 print nextexecution
        return nextexecution

