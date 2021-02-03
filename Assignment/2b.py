import socket
import sys
Tcp_Ip='127.0.0.1'
Tcp_Port=6000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
    c.connect((Tcp_Ip,Tcp_Port))
    msg="welcome to socket programming"
    c.send(msg.encode('utf-8'))
    data=c.recv(1024)
    print("recieved data",data.decode('utf-8'))
