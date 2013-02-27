#!/usr/bin/env python3

""" sup.py : Initializer """

__author__ = "<author>"
__date__ = "2013/01/31"


import argparse
import logging
from pages import WebServer

import cherrypy


def main():
    """ Default main function """
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()

    cherrypy.quickstart(WebServer())



if __name__ == "__main__":
    main()


