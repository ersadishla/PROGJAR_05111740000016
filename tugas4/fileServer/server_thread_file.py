from socket import *
import socket
import threading
import logging
import time
import sys

from file_machine import FileMachine

fm = FileMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = self.connection.recv(64)
            if data:
                d = data.decode()
                hasil = fm.proses(d, self.connection)
                hasil = hasil + "\r\n"
                self.connection.sendall(hasil.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.ip = "localhost"
        self.port = 9799
        self.clients = []
        self.sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.sockets.bind( (self.ip, self.port) )
        self.sockets.listen(1)
        
        print("________________________________________________________\n")
        print(f"Starting server on {self.ip} port {self.port}")
        print("________________________________________________________\n")

        while True:
            self.connection, self.client_address = self.sockets.accept()
            print(f"New connection from {self.client_address[0]} port {self.client_address[1]}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.clients.append(clt)

if __name__ == "__main__":
    svr = Server()
    svr.start()

