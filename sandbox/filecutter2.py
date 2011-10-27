#!/usr/bin/env python
#########################################################
#	Name: 	filecutter2.py		#
#	Description: TODO	#
#########################################################
def copypart(src,dest,start,length,bufsize=1024*1024):
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

if __name__ == '__main__':
    GIG = 2**30
    copypart('test.bin','test2.bin',1*GIG,8*GIG)

