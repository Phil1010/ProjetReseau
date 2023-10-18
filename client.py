import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 8080))
s.send(bytes("Hello serveur", "utf-8"))
data = s.recv(256)
print(data)