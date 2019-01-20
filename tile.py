"""This module contains the Tile class, and its subclasses for monopoly, which represent a location on the gameboard."""
from typing import Any


class Tile:
    """This class represents a spot on the board."""

    def __init__(self, name: str, canbeowned: bool):
        """A tile has name, a list of players occupying it, and an owner. When initialized it should have
        no occupying players or owner."""
        self.name = name
        self.owner = None
        self.canbeowned = canbeowned

    def change_owner(self, person: Any):
        """If the tile can be bought, this will allow change in ownership"""
        if self.canbeowned is True:
            self.owner = person
            self.canbeowned = False


class PropertyTile(Tile):
    """Represents a Tile that can be owned by a player to extract rent from other players who land on it."""

    def __init__(self, name: str):
        """Initializes a property tile. (ie one that can be bought and recieves rent)"""
        Tile.__init__(self, name, True)
        self.development = ""
        self.rent = 0

    def develop(self, amount: int):
        """This function allows the player to develop a building on the property."""
        if amount == 1000 and self.development == "":
            self.development = "Hostel"
            self.rent = 10
        elif amount == 3000 and self.development == "":
            self.development = "B & B"
            self.rent = 20
        elif amount == 7000 and self.development == "":
            self.development = "Hotel"
            self.rent = 50


class TaxTile(Tile):
    """Represents a Tile that taxes those who occupy it."""

    def __init__(self, name: str, amount: int):
        """Initializes a tax tile."""
        Tile.__init__(self, name, False)
        self.tax = amount


class IncomeTile(Tile):
    """Represents a Tile that provides income for those that visit it."""

    def __init__(self, name: str, amount: int):
        """Initializes an income tile."""
        Tile.__init__(self, name, False)
        self.moneyearned = amount
