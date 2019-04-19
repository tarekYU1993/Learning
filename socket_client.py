#! /usr/bin/env python

from socket import *
from time import ctime

Host = '10.64.165.39'
Port = 7800
Buffsize = 1024
Addr = (Host,Port)

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(Addr)

while True:
	data = raw_input('input data:')
	if not data:
		break
	client_socket.send(data)
	data = client_socket.recv(Buffsize)
	if not data:
		break
	print data
client_socket.close()
