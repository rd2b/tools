#!/usr/bin/env python
#########################################################
#	Name: 	fileclient.py		#
#	Description: TODO	#
#########################################################
# -*- coding: UTF-8 -*-
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
print s.pow(2,3)  # Returns 2**3 = 8
print s.add(2,3)  # Returns 5
print s.div(5,2)  # Returns 5//2 = 2

# Print list of available methods
print s.system.listMethods()