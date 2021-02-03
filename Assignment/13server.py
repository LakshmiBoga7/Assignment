import socket
import sys
host=gethostname()
addrs=socket.gethostbyname(host)
port=6000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created")
s.bind((addrs,port))
s.listen(3)
print("waiting for connection")
c,addr=s.accept()
print("Received a connection from",addr)
while True:
    data=c.recv(1024)
    if not data:
        break
    print("from connected user:",data.decode('utf-8'))
    c.send(data)
c.close()
s.close()
