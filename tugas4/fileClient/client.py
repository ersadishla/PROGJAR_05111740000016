import sys
import socket
import os
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9799)
print(f"Connecting to {server_address[0]} port {server_address[1]}")
sock.connect(server_address)

while True:
    string = input()
    cstring = string.split(" ")
    try:
        command = cstring[0].strip()
        if command == 'upload':
            file_name = cstring[1].strip()
            if os.path.exists(file_name):
                sock.sendall(string.encode())

                size = os.path.getsize(file_name)
                print(size)
                val = size.to_bytes(4, byteorder='big')
                sock.send(val)

                print(f"uploading {file_name}")
                with open(file_name, 'rb') as file_to_send:
                    for byte in file_to_send:
                        sock.sendall(byte)
                file_to_send.close()
                response = sock.recv(1024)
                responses = response.decode()
                string_response = json.loads(responses[:-2])
                print(string_response)
            else:
                print('Cannot found file in fileClient directory')

        elif command == 'download':
            sock.sendall(string.encode())
            download_size = sock.recv(4)
            file_size = int.from_bytes(download_size, byteorder='big')
            if file_size :
                file_name = cstring[1].strip()
                with open(file_name, 'wb+') as file_recv:
                    recv_size = 0
                    while recv_size < file_size:
                        byte_n = sock.recv(2)
                        recv_size += len(byte_n)
                        if not byte_n:
                            break
                        file_recv.write(byte_n)
                file_recv.close()
            response = sock.recv(1024)
            responses = response.decode()
            string_response = json.loads(responses[:-2])
            print(string_response)

        elif command == 'list':
            sock.sendall(string.encode())
            response = sock.recv(1024)
            responses = response.decode()
            list_response = json.loads(responses[:-2])
            for objects in list_response:
                i,j = objects.values()
                print(f'{i}\t-updated {j}')

        else:
            print("Command Not Found")
    except:
        print("Error")
