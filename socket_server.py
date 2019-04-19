#!/usr/bin/env python

from socket import *
from time import ctime

Host = ''
Port = 7900
Buffsize = 1024
Addr = (Host,Port)

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(Addr)
server_socket.listen(5)

while True:
	print 'waiting for connection...'
	client_socket,addr = server_socket.accept()
	print '...connection form:',addr

	while True:
		data = client_socket.recv(Buffsize)
		if not data:
			break
		print data
		client_socket.send('%s:%s'%(ctime(),data))
        client_socket.close()
server_socket.close()

