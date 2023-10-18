import socket
import board
import json
import ship

board = board.Board()
j = json.dumps(board.grid)
d = j.encode()

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 5050))
server_socket.listen(1)
(client_socket, client_address) = server_socket.accept()

ships_json = client_socket.recv(1024)
ships=json.loads(ships_json.decode())
board.ships = ships

print(board.ships)

client_socket.send(d)
client_socket.close()
server_socket.close()