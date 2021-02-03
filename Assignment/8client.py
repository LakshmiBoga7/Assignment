import socket
import json

HOST = '127.0.0.1'
PORT = 6000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
l1 = [1,2,3,4,5,6]
data = json.dumps({"a":l1})
s.send(data.encode('utf-8'))

data = s.recv(1024)
data = json.loads(data)
s.close()
print ('Received')
