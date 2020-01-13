import socket


def main():
    host = '192.168.1.7'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)

    c, addr = s.accept()

    print("Connection from" + str(addr))

    while True:
        data = c.recv(1024)

        if not data:
            break

        print("from connected user" + str(data))
        data = str(data.decode('utf-8')).upper()

        print("sending: " + str(data))
        c.send(data.encode('utf-8'))

    c.close()


if __name__ == "__main__":
    main()
