#!/usr/bin/env python
#########################################################
#	Name: 	myfilesplitter.py		#
#	Description: TODO	#
#########################################################

import os

def getpart(src,dest,start,length,bufsize=1024 * 1024):
    f1 = open(src,'rb')
    f1.seek(start)

    f2 = open(dest,'wb')

    while length:
        chunk = min(bufsize,length)
        data = f1.read(chunk)
        f2.write(data)
        length -= chunk
    
    f1.close()
    f2.close()

#-------------------------------------
# Description : TODO 
#-------------------------------------
def split(f, splitsize = 1024 * 1024  ):
    size = os.path.getsize(f)
    print "File size is %s" % size
    nbblocks = size / splitsize
    for i in range(0, size / splitsize +1 ):
        mypos = i * splitsize
        print "Reading {0} block at position {1}".format(i, mypos)
        getpart(f, f + ".split.%s" % i, mypos , splitsize)


if __name__ == '__main__':
    myfile = "/home/remi/tmp/binarytest.ori"
    split(myfile)
