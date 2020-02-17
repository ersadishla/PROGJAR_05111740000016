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
    sock.send(fname.encode())

    sname = 'recv_file'
    with open(sname, 'wb') as file:
        data = sock.recv(1024)
        while data:
            file.write(data)
            data = sock.recv(1024)
    file.close()
except:
    print("error")

finally:
    print("closing")
    sock.close()
