import socket
import sys
Tcp_Ip='127.0.0.1'
Tcp_Port=6000

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((Tcp_Ip,Tcp_Port))
for x in range(1,3):
    msg="Welcome to socket programming"
    c.send(msg.encode('utf-8'))
    
    data=c.recv(1024)
    print("received data",data.decode('utf-8'))
c.close()
