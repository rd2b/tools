#!/usr/bin/env python

""" sortedvsunsorted.py : Which is faster sorted or unsorted array ? """

__author__ = "Remi Debay"
__date__ = "2013/02/13"


import argparse
import random
import time

def describearray(myarray = None, loops = 100):
    didif=0
    arraylen = len(myarray)
    for i in range(loops):
        for value in myarray:
            if ( value < 500):
                didif += 1
    return didif



def main():
    """ Default main function """
    sortedarray = []
    unsortedarray = []
    loops = 10
    elements = 10*1000*1000



    for i in range(elements):
        unsortedarray.append(random.randint(0,1000))

    print("Sort:")
    start_time = time.time()
    sortedarray = sorted(unsortedarray)
    print(time.time() - start_time)

    print("Unsorted:")
    start_time = time.time()
    unsorteddidif = describearray(unsortedarray, loops)
    print(time.time() - start_time)
    
    print("Sorted:")
    start_time = time.time()
    sorteddidif = describearray(sortedarray, loops)
    print(time.time() - start_time)

    




if __name__ == "__main__":
    main()


