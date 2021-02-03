import socket
import sys
import json

HOST, PORT = "localhost", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")
sock.bind((HOST,PORT))
sock.listen(3)
print("waiting for connection")
c,addr=sock.accept()
print("Received a connection from",addr)
while True:
    data=c.recv(1024)
    
    data=json.loads(data.decode('utf-8'))
    print("received ",data)

c.close()
    



    
