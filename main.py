import board
import ship
import player
import bot

bot = bot.Bot(board.Board())
bot.add_ship_bot()
bot.add_ship_bot()
bot.add_ship_bot()


print(bot.board.display_ships())
