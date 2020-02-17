import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    fname = input("input filename and its extension : ")
    with open(fname, 'rb') as file:
        sock.sendfile(file, 0)
except:
    print("error")

finally:
    print("closing")
    sock.close()
