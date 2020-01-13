import socket


def main():
    host = '192.168.1.7'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("-> ")

    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024)
        print("Received from Server:- " + data.decode('utf-8'))
        message = input("-> ")

    s.close()


if __name__ == "__main__":
    main()
