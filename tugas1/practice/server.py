import sys
import socket
import _thread

def initSocket( port_number ):
    server_address = ('0.0.0.0', port_number)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"start server on {server_address[0]} port {server_address[-1]}")
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print(f"waiting for connection {server_address[-1]}")
        connection, client_address = sock.accept()
        print(f"connection from {client_address}")
        # Receive the data in small chunks and retransmit it
        text = ''
        while True:
            data = connection.recv(16)
            text += data.decode()
            print(f"received {data}")
            if data:
                print("sending back data")
                connection.sendall(data)
            else:
                print(text)
                print(f"no more data from {client_address}")
                break
        # Clean up the connection
        connection.close()

try:
    _thread.start_new_thread( initSocket, (31001, ) )
    _thread.start_new_thread( initSocket, (31002, ) )
    _thread.start_new_thread( initSocket, (31003, ) )
except:
    print("Error: unable to start thread")

while True:
   pass
