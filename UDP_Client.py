import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# SOCK_DGRAM means connection oriented TCP protocol

s.connect(('', 1247)) #Enter the IP address of the server in ''
#IP address of server

a = raw_input("Input(numbers seperated by spaces): ")
s.send(str(a))

print s.recv(4096)

s.close()
