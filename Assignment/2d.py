import socket
import sys
Tcp_Ip='127.0.0.1'
Tcp_Port=6000
class TcpClient:
    def __enter__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self
    def __exit__(self,exc_type, exc_value, traceback):
        self.sock.close()
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
    with TcpClient() as c:
        c.connect('127.0.0.1',6000)
        c.mysend("welcome to socket programming")
        msg=c.myrecv()
        print("received data",msg)
    
