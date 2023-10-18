import board
import ship
import player

player1 = player.Player("Player1", board.Board())
player1.board.display_init()

player1.board.add_ship(ship.Ship(0, 0, 2, "horizontal"))
player1.board.add_ship(ship.Ship(4, 5, 4, "vertical"))

player1.board.display_ships()

print("Le plateau du premier joueur : " + player1.name)


x = int(input("Entrez la coordonnée X du tir : "))
y = int(input("Entrez la coordonnée Y du tir : "))
x2 = int(input("Entrez la coordonnée X du tir : "))
y2 = int(input("Entrez la coordonnée Y du tir : "))
player1.board.shot(x, y)
player1.board.shot(x2, y2)

player1.board.display_board()
