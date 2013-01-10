#!/usr/bin/env python
#########################################################
#	Name: 	cutup.py		#
#	Description: TODO	#
#########################################################
# -*- coding: UTF-8 -*-

#-------------------------------------
# Description : TODO 
#-------------------------------------
def readfile(filepath):
    blocksize = 1024 * 4
    with open(filepath) as f:
        while not f.closed :
            block = readfileblock(f, blocksize)
            print block
    
#-------------------------------------
# Description : TODO 
#-------------------------------------
def readfileblock(openfile, blocksize):
    content = openfile.read(blocksize)
    return None
    

readfile("/var/log/dmesg")
