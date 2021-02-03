import socket

host='127.0.0.1'
port=6000

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect((host,port))

    """ Opening and reading the file data. """
    file = open("data.txt", "r")
    data = file.read()

    """ Sending the filename to the server. """
    client.send("data.txt".encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    

    """ Sending the file data to the server. """
    client.send(data.encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    print("received data ",msg)

    """ Closing the file. """
    file.close()

    """ Closing the connection from the server. """
    client.close()


if __name__ == "__main__":
    main()
