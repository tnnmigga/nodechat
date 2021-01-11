import socket
import threading
import time

server_host = '127.0.0.1'
server_port = 8888


class Client:
    def __init__(self):
        self.porn = None
        self.uname = None
        self.host = socket.gethostbyname(socket.gethostname())

    def login(self):

        while True:
            self.uname = input('what is your name?\n')
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((server_host, server_port))
            connection.send(self.uname.encode())
            msg = connection.recv(10).decode()
            if msg[0:2] == 'ok':
                print('connect seccessful')
                return True
            else:
                print('username error')
            connection.close()

    def recv_msg(self):
        def receiver(recv_socket):
            while (True):
                msg, _ = recv_socket.accept()
            print(msg.decode())

        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        recv_socket.bind((self.host, self.porn))
        recv_socket.listen(5)
        threading.Thread(receiver, (recv_socket,)).start()

    def send_msg(self):
        def sender():
            while True:
                msg = input()
                send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                send_socket.connect((server_host, server_port))
                send_socket.send(msg.encode())
                send_socket.close()
        threading.Thread(sender).start()

if __name__ == '__main__':
    client = Client()
    client.login()
    client.recv_msg()
    client.send_msg()
