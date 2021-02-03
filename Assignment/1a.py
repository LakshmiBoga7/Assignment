import socket
import sys
Tcp_Ip='127.0.0.1'
Tcp_Port=6000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created")
s.bind((Tcp_Ip,Tcp_Port))
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
