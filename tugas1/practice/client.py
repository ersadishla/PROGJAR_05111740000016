import sys
import socket
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
port_number = int(input("input port number : "))
server_address = ('10.151.63.23', port_number)
try:
    print(f"connecting to {server_address}")
    sock.connect(server_address)
except:
    print("port not found")
    port_list = [31001, 31002, 31003]
    server_address = ('10.151.63.23', random.choice(port_list))
    print(f"connecting to {server_address}")
    sock.connect(server_address)

try:
    # Send data
    message = input("input text messages : ")
    # message = 'PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA'
    print(f"sending {message}")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f"{data}")
finally:
    print("closing")
    sock.close()
