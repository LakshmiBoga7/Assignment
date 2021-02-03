import socket
import sys
Tcp_Ip='127.0.0.1'
Tcp_Port=6000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((Tcp_Ip,Tcp_Port))
    s.listen(3)
    (c, addr)=s.accept()
    with c:
        print("Receive a connect from ",addr)
        while True:
            data=c.recv(1024)
            if not data:
                break
            print(" client says :",data.decode('utf-8'))
            c.send(data)
    
    
