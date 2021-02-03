import socket

sock = socket.socket()
host = '127.0.0.1'
port = 6000

print('Waiting for connection')
try:
    sock.connect((host, port))
except socket.error as e:
    print(str(e))

Response = sock.recv(1024)
while True:
    Input = input('Say Something: ')
    sock.send(str.encode(Input))
    Response = sock.recv(1024)
    print(Response.decode('utf-8'))

sock.close()
