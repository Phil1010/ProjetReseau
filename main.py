import board
import ship
import player
import bot

player1 = player.Player("PVP", board.Board())
player1.board.add_ship(ship.Ship(0, 0, 2, "v"))
player1.board.add_ship(ship.Ship(3, 3, 3, "v"))
player1.board.add_ship(ship.Ship(4, 4, 4, "v"))

bot1 = bot.Bot(board.Board())
bot1.add_ship_bot()
bot1.add_ship_bot()
bot1.add_ship_bot()


x, y = bot1.shot()
player1.board.shot(x, y)


print(player1.board.display_board())
print(bot1.board.display_ships())
print(bot1.board.display_board())
print(bot1.board.display_board_without_ships())
print("tirs réussis : " + str(player1.board.hit_shots))
print("tirs ratés : " + str(player1.board.missed_shots))
