import board
import ship
import player

player1 = player.Player("Player1", board.Board())
player1.board.add_ship(ship.Ship(0, 0, 2))
player1.board.add_ship(ship.Ship(4, 5, 4))

player2 = player.Player("Player2", board.Board())
player2.board.add_ship(ship.Ship(1, 1, 2))
player2.board.add_ship(ship.Ship(6, 4, 3))

print("Le plateau du premier joueur : " + player1.name)
player1.board.display_init()
print("Le plateau du deuxième joueur : " + player2.name)
player2.board.display_init()

x = int(input("Entrez la coordonnée X du tir : "))
y = int(input("Entrez la coordonnée Y du tir : "))
x2 = int(input("Entrez la coordonnée X du tir : "))
y2 = int(input("Entrez la coordonnée Y du tir : "))
player1.board.shot(x, y)
player1.board.shot(x2, y2)

player1.board.display_board()
