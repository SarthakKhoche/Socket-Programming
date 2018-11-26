import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_DGRAM means connection oriented TCP protocol

port = 1260

s.bind(('', port))

s.listen(1)

c, addr = s.accept()

while True:
   recv_input = c.recv(2048)
   if not recv_input: break
   arr = map(int, recv_input.split(' '))
   arr.sort()
   c.send(str(arr))

c.close()
