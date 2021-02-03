import socket
import os
from _thread import *
sock=socket.socket()
host='127.0.0.1'
port=6000
ThreadCount=0
try:
    sock.bind((host,port))
except socket.error as e:
    print(str(e))
print("waiting for connection")
sock.listen(5)
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = sock.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
