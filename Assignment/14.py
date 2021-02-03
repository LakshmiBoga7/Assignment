import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.example.com',80))
s.send(b"GET / HTTP/1.1\r\n Host:www.example.com\r\n\r\n")
while True:
    data=s.recv(1024)
    if (len(data))<1:
        break
    print(data)
s.close()
    
