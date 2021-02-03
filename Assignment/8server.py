import socket
import json

HOST = '127.0.0.1'
PORT = 6000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)
conn,addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(4096)
    data =json.loads(data.decode('utf-8'))
    li=data.get("a")
    
conn.close()
