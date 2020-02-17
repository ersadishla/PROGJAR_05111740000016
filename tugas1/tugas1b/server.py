import socket
import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print(f"starting up on {server_address[0]} port {server_address[1]}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("waiting for a connection")

    connection, client_address = sock.accept()
    print(f"connection from {client_address}")

    fname = connection.recv(128)
    print(fname.decode())

    with open(fname.decode(), 'rb') as file:
        connection.sendfile(file, 0)
    file.close()

    connection.close()
