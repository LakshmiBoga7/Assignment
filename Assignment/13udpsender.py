import socket
import sys
host=gethostname()
addrs=socket.gethostbyname(host)
port=6000

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("server socket created")

s.bind((addrs,port))
while True:
    data,addr=s.recvfrom(1024)
    
    print("received data from {1} and {2}",data,addr)
    s.sendto(data,addr)
    
s.close()
    
        
