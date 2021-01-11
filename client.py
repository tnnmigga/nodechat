import socket
import threading

server_host = '127.0.0.1'
server_port = 10086


class Client:
    def __init__(self):
        self.port = None
        self.uname = None
        self.host = '127.0.0.1'  # socket.gethostbyname(socket.gethostname())

    def login(self):

        while True:
            self.uname = input('what is your name?\n')
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((server_host, server_port))
            connection.send(('~%s~#~%s~#~%s~' %
                             ('login', self.uname, '')).encode())
            msg = connection.recv(10).decode()
            if msg[0:2] == 'ok':
                print('connect seccessful')
                self.port = int(msg[2:])
                return True
            else:
                print('login unsuccessful: ' + msg)
            connection.close()

    def recv_msg(self):
        def receiver():
            recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            recv_socket.bind((self.host, self.port))
            recv_socket.listen(5)
            while (True):
                connection, _ = recv_socket.accept()
                msg = connection.recv(1024).decode()
                connection.close()
                print(msg)

        threading.Thread(target=receiver).start()

    def send_msg(self):
        def sender():
            while True:
                msg = input()
                send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                send_socket.connect((server_host, server_port))
                send_socket.send(('~%s~#~%s~#~%s~' %
                                  ('msg', self.uname, msg)).encode())
                send_socket.close()

        threading.Thread(target=sender).start()


if __name__ == '__main__':
    client = Client()
    client.login()
    client.recv_msg()
    client.send_msg()
