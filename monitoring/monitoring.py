#!/usr/bin/env python

""" monitoring.py : Monitoring Server and client with web Overview """

__author__ = "Remi Debay"
__date__ = "2013/02/27"


import argparse


def main():
    """ Default main function """
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()
    print args.accumulate(args.integers)


if __name__ == "__main__":
    main()


