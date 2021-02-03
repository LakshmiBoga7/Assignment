import socket
import sys
class TcpClient:
    def __init__(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def connect(self,Tcp_Ip,Tcp_Port):
        self.sock.connect((Tcp_Ip,Tcp_Port))
    def mysend(self,msg):
        self.sock.send(msg.encode('utf-8'))
    def myrecv(self):
        data=self.sock.recv(1024)
        if not data:
            return None
        return data.decode('utf-8')
    def __del__(self):
        self.sock.close()
if __name__ == "__main__":
    c=TcpClient()
    c.connect('127.0.0.1',6000)
    c.mysend("Welocme to socket programming")
    msg=c.myrecv()
    print("Received data",msg)
