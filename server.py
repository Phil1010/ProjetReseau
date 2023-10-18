import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))
s.listen(5)

while True:
    (clientsocket, address) = s.accept()
    data = clientsocket.recv(256)
    print("connexion")
    print(data)
    clientsocket.send(bytes("hello client", "utf-8"))
