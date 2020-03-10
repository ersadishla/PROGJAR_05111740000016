
import socket

TARGET_IP = "10.151.254.27"
TARGET_PORT = 5006

message = "Ersad Ahmad Ishlahuddin"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(message.encode()),(TARGET_IP,TARGET_PORT))