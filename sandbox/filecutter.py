#!/usr/bin/env python
#########################################################
#	Name: 	filecutter.py		#
#	Description: TODO	#
#########################################################
fn = '/home/remi/tmp/binarytest.ori'
 
# Split into 4 files
f = open(fn, 'rb')
data = f.read()
f.close()
 
bytes = len(data)
inc = (bytes+4)/4
fileNames = []
for i in range(0, bytes+1, inc):
    fn1 = "file%s" % i
    fileNames.append(fn1)
    f = open(fn1, 'wb')
    f.write(data[i:i+inc])
    f.close()
 
new_file = '/home/remi/tmp/binarytest.end'
dataList = []
 
for fn in fileNames:
    f = open(fn, 'rb')
    dataList.append(f.read())
    f.close()
 
f = open(new_file, 'wb')
for data in dataList:
    f.write(data)
f.close()


