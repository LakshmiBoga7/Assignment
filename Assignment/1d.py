import socket
import sys

Tcp_Ip="127.0.0.1"
Tcp_Port=1500


class TcpServer:
    def __enter__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.Tcp_Ip, self.Tcp_Port))
        self.sock.listen()
        return self
    def __exit__(self,exc_type, exc_value, traceback):
        self.sock.close()
    def __init__(self,Tcp_Ip,Tcp_Port):
        self.Tcp_Ip=Tcp_Ip
        self.Tcp_Port=Tcp_Port     
    def accept(self):
        client, addr = self.sock.accept()
        print("Received a connection from", addr)
        self.client = client

    def mysend(self, msg):
        self.client.send(mystr.encode('utf-8'))
        
    def myrecv(self):
        data = self.client.recv(1024)
        if not data: return None
        return data.decode('utf-8')
            
    def __del__(self):
        self.sock.close()
        
if __name__ == "__main__":
    
    with TcpServer("127.0.0.1",1600) as server:
        server.accept()
        while True:
            msg = server.myrecv()
            if msg == None : break
            server.mysend(msg)
    

