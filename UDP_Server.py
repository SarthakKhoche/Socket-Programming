import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# SOCK_STREAM means connection oriented TCP protocol

port = 1247 #Random

s.bind(('', port))

while True:
   recv_input, addr = s.recvfrom(2048)
   if not recv_input: break
   arr = map(int, recv_input.split(' '))
   arr.sort()
   arr.reverse()
   s.sendto(str(arr), addr)

s.close()
