#!/usr/bin/env python
"""
To Use This Script first run telegram-cli like this: 
	telegram-cli -W -k tg-server.pub -D -vvv -d -E -R -C -P 2391

	You can use any port number (and of course you need to use the correct port withn the script)
	if you are running telegram-cli for the first time first run it without the switches to create server public key file (for do it in any hard way you know) and then run the deamon code above

"""

import socket
import sys


if len(sys.argv)<5 or len(sys.argv)>6:
	print "Usage %s port photo|video|document|file|audio user file [description]" % (sys.argv[0])
	sys.exit(-1)
code=0
host = 'localhost'
port = int(sys.argv[1])                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	print "Sending file [%s] to Telegram ..." % (sys.argv[4])
	s.connect((host, port))
	command=b"send_%s %s \"%s\"" % (sys.argv[2],sys.argv[3],sys.argv[4].replace('"', r'\"'))
	if len(sys.argv)==6:
		command += " \"%s\" " %(sys.argv[5].replace('"', r'\"'))
	#print command
	s.sendall(command+" \n")
	data = s.recv(1024)
	if 'SUCCESS' in data:
		print "SUCCESS"
	else:
		print "Failure"
		code=-1
		print repr(data)
finally:
	s.close()	
sys.exit(code)

