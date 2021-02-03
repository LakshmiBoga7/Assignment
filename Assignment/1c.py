import socket
import sys
class TcpServer:
    def __init__(self,Tcp_Ip,Tcp_Port):
        self.Tcp_Ip=Tcp_Ip
        self.Tcp_Port=Tcp_Port
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((self.Tcp_Ip,self.Tcp_Port))
        self.sock.listen()
        
    def accept(self):
        c,addr=self.sock.accept()
        print("Received Connection From",addr)
        self.c=c
    def mysend(self,msg):
        self.c.send(msg.encode('utf-8'))
    def myrecv(self):
        data=self.c.recv(1024)
        if not data:
            return None
        return data.decode('utf-8')
    def __del__(self):
        self.sock.close()
if __name__ == "__main__":
    s=TcpServer('127.0.0.1',6000)
    s.accept()
    while True:
        msg=s.myrecv()
        if msg==None:
            break
        s.mysend(msg)
