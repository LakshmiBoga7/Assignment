import socket
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("server socket created")
host='127.0.0.1'
port=6000
s.bind((host,port))
while True:
    data,addr=s.recvfrom(1024)
    
    print("received data from {1} and {2}",data,addr)
    s.sendto(data,addr)
    
s.close()
    
        
