import socket
import time
import pickle
host='127.0.0.1'
port=6000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port ))
s.listen(3)

while True:
    
    c, addr = s.accept()
    print("Received connection from",addr)

    d = {1:"Hai", 2: "Hello"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{10}}", 'utf-8')+msg
    print(msg)
    c.send(msg)
