import socket

T_PORT = 60
TCP_IP = '127.0.0.1'
BUF_SIZE = 1024
MSG = input("Skriv: ")
# create a socket object name 'k'

k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
k.connect((TCP_IP, T_PORT))
k.send(MSG.encode('utf-8'))
data = k.recv(BUF_SIZE)
text = k.recv(BUF_SIZE)
print(text.decode('utf-8'))
k.close
