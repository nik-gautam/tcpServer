import socket
import sys


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 6969
        s = socket.socket()

    except socket.error as msg:
        print("Connection Error: \n" + str(msg) + "\n Exiting....")


def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding socket, Port Number:- " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Binding Error: \n" + str(msg) + "\n Retrying....")
        bind_socket()


def socket_accept():
    conn, address = s.accept()
    print("Connection Established!!\n IP:-" +
          address[0] + " PORT:- " + str(address[1]))

    send_command(conn)

    conn.close()


def send_command(conn):
    while True:
        cmd = input()

        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_res = str(conn.recv((1024)), "utf-8")
            print(client_res, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


if __name__ == '__main__':
    main()
