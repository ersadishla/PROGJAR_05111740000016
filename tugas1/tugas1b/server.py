import sys
import socket
import _thread

def initSocket( port_number ):
    server_address = ('127.0.0.1', port_number)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"start server on {server_address[0]} port {server_address[-1]}")
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print("waiting for a connection")

        connection, client_address = sock.accept()
        print(f"connection from {client_address}")

        fname = connection.recv(128)
        print(fname.decode())

        try:
            with open(fname.decode(), 'rb') as file:
                connection.sendfile(file, 0)
            file.close()
        except:
            print("unable to open file")

        connection.close()

try:
    _thread.start_new_thread( initSocket, (31001, ) )
    _thread.start_new_thread( initSocket, (31002, ) )
    _thread.start_new_thread( initSocket, (31003, ) )
except:
    print("Error: unable to start thread")

while True:
   pass

