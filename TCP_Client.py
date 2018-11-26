import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_STREAM means connection oriented TCP protocol

port = 1260

s.connect(('', port)) #Enter the IP address of the server in ''
#IP address of server

a = raw_input("Input(Numbers seperated by spaces): ")
s.send(str(a))

print s.recv(4096)

s.close()
