#!/usr/bin/python3
import socket 
import sys

#remote_server = sys.argv[1]
#rsocket = (remote_server, 80)
#rfile = sys.argv[2]
sock =  socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.connect(('w3.org', 80))
cmd = 'GET https://www.w3.org/TR/PNG/utf-8.txt HTTP/1.0\n\n'.encode()
sock.send(cmd)

while True:
    data = sock.recv(512)
    if len(data) < 1:
        break
    with open('ouput.txt', 'ba') as f:
        f.write(data)

sock.close()
