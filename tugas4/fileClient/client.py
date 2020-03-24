import sys
import socket
import os
import json
import time

if __name__ == "__main__":
    try:
        server_address = ("localhost", 9799)
        print(f"Connecting to server {server_address[0]}:{server_address[1]}")
        time.sleep(1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
    except:
        print("Unable to reach server")
        print("Exiting...")
        exit(-1)

    print("Server Connected!\n")
    while True:
        string = input("(alprotokol)> ")
        cstring = string.split(" ")

        try:
            command = cstring[0].strip()
            
            if command == 'upload':
                file_name = cstring[1].strip()
                if os.path.exists(file_name):
                    sock.sendall(string.encode())

                    size = os.path.getsize(file_name)
                    val = size.to_bytes(4, byteorder='big')
                    sock.send(val)

                    print(f"Uploading...")
                    with open(file_name, 'rb') as file_to_send:
                        for byte in file_to_send:
                            sock.sendall(byte)
                    file_to_send.close()
                    response = sock.recv(1024)
                    responses = response.decode()
                    print(responses)
                else:
                    print('Cannot found file in fileClient directory')

            elif command == 'download':
                sock.sendall(string.encode())
                download_size = sock.recv(4)
                file_size = int.from_bytes(download_size, byteorder='big')
                if file_size :
                    print(f"Downloading...")
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
                print(responses)

            elif command == 'list':
                sock.sendall(string.encode())
                response = sock.recv(1024)
                responses = response.decode()
                print(responses)

            else:
                print("Command Not Found")
        except:
            print("Error")
