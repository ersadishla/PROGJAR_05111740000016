import socket
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
port_number = int(input("input port number : "))
server_address = ('127.0.0.1', port_number)
try:
    print(f"connecting to {server_address}")
    sock.connect(server_address)
except:
    print("port not found")
    port_list = [31001, 31002, 31003]
    server_address = ('127.0.0.1', random.choice(port_list))
    print(f"connecting to {server_address}")
    sock.connect(server_address)

try:
    # Send data
    fname = input("input filename and its extension : ")
    with open(fname, 'rb') as file:
        sock.sendfile(file, 0)
    file.close()
    print("success, check from_client")
except:
    print("error")

finally:
    print("closing")
    sock.close()
