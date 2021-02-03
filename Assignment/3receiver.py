import socket
host='127.0.0.1'
port=6000
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=b"Hello Programming"
sock.sendto(msg,(host,port))
data,addr=sock.recvfrom(1024)
print("received data :",data,addr)

