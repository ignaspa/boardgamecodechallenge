"""
run this file to play the game in the terminal!
"""
from player import Player
from gameboard import GameBoard

if __name__ == "__main__":

    players = []

    print("Welcome to the <redacted company> intern challenge monopoly game by Ignas!")
    print('...instructions go here...')
    name1 = input("Give a name to player 1: ")
    name2 = input("Give a name to player 2: ")
    name3 = input("Give a name to player 3: ")
    name4 = input("Give a name to player 4: ")

    player_one = Player(name1)
    player_two = Player(name2)
    player_three = Player(name3)
    player_four = Player(name4)

    board = GameBoard([player_one, player_two, player_three, player_four])

    i = 0

    while len(board.players) != 1:
        print('It is now ' + board.players[i].name + '\'s turn!')
        board.make_move(board.players[i])
        i += 1
        if i > len(board.players) - 1:
            i = 0
    winner = board.players.pop(0)
    print(winner.name + " won! :D")
