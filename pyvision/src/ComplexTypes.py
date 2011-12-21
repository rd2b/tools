
class Alert(object):
    id = None
    def __init__(self, date=None, 
                       sender=None, 
                       reference=None, 
                       message=None,
                       priority=0):
        self.date = date
        self.sender = sender
        self.reference = reference
        self.message = message
        self.priority = priority

    def __repr__(self):
        return "<Alert('%s','%s', '%s')>" % (self.date,
               self.sender, self.reference, self.message, str(self.priority))
