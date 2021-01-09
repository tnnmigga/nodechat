import socket
import threading
import time

server_host = ''
server_port = ''

class Client:

    def login(self, host, port):
        
        while True:
            self.uname = input('what is your name?')
            connection = socket.socket()
            connection.connect((server_host, server_port))
            connection.send(self.uname)
            msg = connection.recv(10)
            if msg == 'ok':
                print('connect seccessful')
                return True
            else:
                print('username error')
            connection.close()
            
    def recv_msg(self, porn):
        host = socket.gethostbyname()
        recv_server = socket.socket()