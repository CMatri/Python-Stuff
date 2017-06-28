import socket


TCP_IP = '10.1.10.1'
TCP_PORT = 22
BUFFER_SIZE = 2048
MESSAGE = 'F'*20

print "connecting..."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print "sending..."
s.send(MESSAGE)
print "receiving..."
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data