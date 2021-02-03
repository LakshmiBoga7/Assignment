import socket
host='127.0.0.1'
port=6000
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(3)
    while True:
        c,addr=s.accept()
        print("received a connection from",addr)
        """ Receiving the filename from the client. """
        filename=c.recv(1024).decode('utf=8')
        file=open(filename,"w")
        c.send("file received".encode('utf-8'))
        """ Receiving the file data from the client. """
        data=c.recv(1024).decode('utf-8')
        file.write(data)
        c.send("file data received".encode('utf-8'))
        """ Closing the file. """
        file.close()

        """ Closing the connection from the client. """
        c.close()

if __name__ == "__main__":
    main()
