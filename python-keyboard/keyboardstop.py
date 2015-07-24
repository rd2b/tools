#!/usr/bin/env python

""" keyboardstop.py : Description """

__author__ = "<author>"
__date__ = "2015/07/24"


import argparse
import time
import signal
def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    


def main():
    """ Default main function """
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', type=int, help='foo help')
    args = parser.parse_args()

    signal.signal(signal.SIGINT, signal_handler)

    for n in range(0,args.number):
        for j in range(1,5):
            print("Loop %i, %i"%(n,j))
            time.sleep(1)
            


if __name__ == "__main__":
    main()


