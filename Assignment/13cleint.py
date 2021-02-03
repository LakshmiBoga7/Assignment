import socket
import sys
host=socket.gethostname()
addrs=socket.gethostbyname(host)
port=6000
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((addrs,port))
for x in range(1,3):
    msg="Welcome to Socket Programming"
    c.send(msg.encode('utf-8'))
    data=c.recv(1024)
    print("Received data",data.decode('utf-8'))
c.close()
