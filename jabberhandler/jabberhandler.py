#!/usr/bin/env python
#########################################################
#   Name:   jabberhandler.py     #
#   Description: TODO   #
#########################################################

import sys,os,xmpp,time

tojid=sys.argv[1]
text=' '.join(sys.argv[2:])


def sendmessage(client, recipient, message):
    id = client.send(xmpp.protocol.Message(recipient,message))
    print 'sent message with id',id

def messageConsummer(sess,mess):
    print 'MESSAGE'
    nick=mess.getFrom().getResource()
    text=mess.getBody()
    #print mess,nick
    print text


if len(sys.argv) < 2:
    print "Syntax: xsend JID text"
    sys.exit(0)


jidparams={}
if os.access(os.environ['HOME']+'/.xsend',os.R_OK):
    for ln in open(os.environ['HOME']+'/.xsend').readlines():
        if not ln[0] in ('#',';'):
            key,val=ln.strip().split('=',1)
            jidparams[key.lower()]=val
for mandatory in ['jid','password']:
    if mandatory not in jidparams.keys():
         open(os.environ['HOME']+'/.xsend','w').write('jid=mylogin@domain.net\n#password=password\n')
         print 'Please point ~/.xsend config file to valid JID for sending messages.'
         sys.exit(0)

jid=xmpp.protocol.JID(jidparams['jid'])
cl=xmpp.Client(jid.getDomain(),debug=[])

con=cl.connect()

if not con:
    print 'could not connect!'
    sys.exit()
print 'connected with',con

auth=cl.auth(jid.getNode(),jidparams['password'],resource=jid.getResource())

if not auth:
    print 'could not authenticate!'
    sys.exit()
print 'authenticated using',auth

#cl.SendInitPresence(requestRoster=0)   # you may need to uncomment this for old server
sendmessage(cl, tojid, "I am online")
sendmessage(cl, tojid, text)
cl.RegisterHandler('message',messageConsummer)

while 1:
    cl.Process(1)


time.sleep(1)   # some older servers will not send the message if you disconnect immediately after sending

#cl.disconnect()
