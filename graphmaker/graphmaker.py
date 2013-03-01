#!/usr/bin/env python

""" graphmaker.py : Description """

__author__ = "R 2B"
__date__ = "2013/01/25"


import argparse
import logging


from threading import Thread
from Queue import Queue

class Measure:
    def __init__(self, timestamp, reference, value):
        self.timestamp = timestamp
        self.reference = reference
        self.value = value

    def __str__(self):
        return str({
            "timestamp":str(self.timestamp),
            "reference":str(self.reference),
            "value":str(self.value)
            })

        
class Sender():
    def __init__(self, workers = 5):
        self.workers = []
        for workerid in range(workers):
            logging.debug("Thread %s started", workerid)
            myworker = Thread(targer = self.worker)
            myworker.daemon = True
            myworker.start
            self.workers.append(myworker)

    def handle(self, data):



def main():
    """ Default main function """
    myformat = "%(asctime)s %(message)s"
    logging.basicConfig(level = logging.INFO, format = myformat)

    # parse command line options
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--datas', type=str, 
            default="", help='Url to check' ) 
    parser.add_argument('-S', '--Server', action='store_true' 
            help='Starts as server (default is client)')
    parser.add_argument('-i', '--stdin', action='store_true',
            help='Read input from stdin' )

    args = parser.parse_args()
    print args.accumulate(args.integers)

    if args.Server:
        pass
    else:
        if args.stdin:
            pass


if __name__ == "__main__":
    main()

