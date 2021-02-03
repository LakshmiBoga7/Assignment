import socket
host=socket.gethostname()
port=6000
addrs=socket.gethostbyname(host)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=b"Hello Programming"
sock.sendto(msg,(addrs,port))
data,addr=sock.recvfrom(1024)
print("received data :",data,addr)
