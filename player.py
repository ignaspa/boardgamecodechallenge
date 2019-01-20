"""This module contains the Player Class"""
from tile import *


class Player:
    """This is the class that represents a player. It has attributes that describe the player's
    name, money, assets (ie property), and position on the board."""

    def __init__(self, name: str):
        self.money = 1500
        self.assets = []
        self.name = name
        self.spot = 0

    def advance(self, steps: int):
        """This function will update a player's spot."""
        self.spot += steps
        if self.spot > 27:
            self.spot -= 27

    def spend(self, amount: int):
        """This will decrease a player's money reserves by the amount specified, for taxes, rent, or buying purposes.
        """
        self.money -= amount

    def intake(self, amount: int):
        """This will increase a player's money reserves by the amount specified, either by earning rent or income.
        """
        self.money += amount

    def add_property(self, asset: Tile):
        """This will add a given property to the player's list of assets."""
        self.assets.append(asset)
