from player import Player
from gameboard import GameBoard

players = []

name1 = "Tom"
name2 = "Jonah"
name3 = "Allyson"
name4 = "Rachel"

player_one = Player(name1)
player_two = Player(name2)
player_three = Player(name3)
player_four = Player(name4)

board = GameBoard([player_one, player_two, player_three, player_four])
