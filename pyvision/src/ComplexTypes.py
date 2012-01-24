

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
    def __init__(self, starting, seconds, command):
       self.starting = starting
       self.seconds = seconds
       self.command = commands
    
    def schedule(self):
        if not self.starting:
            self.starting = datetime.now()
        nextexecution = c.starting
        if not self.seconds > 0 :
             delta = timedelta(seconds = self.seconds)
             while nextexecution < datetime.now() and delta:
                 nextexecution = nextexecution + delta
        return nextexecution

