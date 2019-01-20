"""This module contains the GameBoard class."""
import random
from player import Player
from tile import *


class GameBoard:
    """This will be the class that represents the board for monoploy. It has 1 tax tile (which is randomly located), 1
    income tile (which is randomly located), and 26 property tiles."""
    def __init__(self, players: list):
        areas = ["Davenport ", "Melfa ", "Bloor ", "LaSenda ", "Spadina ", "Borrin ", "Kent ", "Yonge ",
                 "Dundas ", "French ", "Davos ", "Coster ", "Surrey ", "Limon ", "York ", "Queen ", "Mercy ",
                 "Garden ", "Jazz ", "Meadow ", "Sarri ", "Glenn ", "Beacon ", "Salt ", "Willow ", "Oak ",
                 "Calm ", "Zanzibar ", "Icarus ", "Key "]
        types = ["Blvd", "Rd", "Ave", "St", "Heights", "Port", "Crescent", "Farms"]

        self.tiles = []

        index_of_tax = random.randint(0, 27)
        index_of_income = index_of_tax - random.randint(0, 27)

        for k in range(0, 28):
            partone = areas.pop(random.randint(0, len(areas) - 1))
            parttwo = types[random.randint(0, len(types) - 1)]
            name = partone + parttwo
            if k == index_of_income:
                self.tiles.append(IncomeTile('INCOME', 200))
            elif k == index_of_tax:
                self.tiles.append(TaxTile('TAX', 100))
            else:
                self.tiles.append(PropertyTile(name))

        self.players = players

    def make_move(self, person: Player):
        """This function will move the Player an additional n spots forward on the board,
        according to a 'roll of the dice' integer n which is between 1 and 6. """
        print('Your balance is: ' + str(person.money))
        roll = random.randint(1, 6)
        person.advance(roll)
        print('You rolled a ' + str(roll))
        position = self.tiles[person.spot]
        print('You landed on ' + str(position.name))

        if isinstance(position, IncomeTile):
            self.give_income(person, position)

        elif isinstance(position, TaxTile):
            self.pay_tax(person, position)

        elif isinstance(position, PropertyTile):
            self.land_on_property(person, position)

        loss = self.check_loss(person)

        if loss:
            self.players.pop(self.players.index(person))
            print(str(person.name) + ' has lost!')

    def give_income(self, person: Player, position: IncomeTile):
        """This allows a player to gain income."""
        print('You have landed on the Income Tile, you gained ' + str(position.moneyearned) + ' dollars!')
        person.intake(position.moneyearned)

    def pay_tax(self, person: Player, position: TaxTile):
        """This allows a player to pay taxes."""
        print('You have landed on the Tax Tile, you owe ' + str(position.tax) + ' dollars!')
        person.spend(position.tax)

    def land_on_property(self, person: Player, position: PropertyTile):
        """This function goes through the process of a person landing on a property tile and either paying rent
        or developing it."""
        if self.check_onsale(person.spot) is True:
            sold = self.develop_spot(position, person)

            if sold == 1:
                position.owner = person
                person.assets.append(position)
                print('Congratulations, you developed the property!')
        else:
            position.owner.intake(min(position.rent, person.money))
            person.spend(position.rent)
            print(position.owner.name + "just gained a few bucks!")

    def check_onsale(self, spot: int):
        """Checks if a given spot is available to purchase."""
        if self.tiles[spot].canbeowned is True:
            return True
        return False

    def develop_spot(self, spot: PropertyTile, person: Player):
        """This function goes through the process of selling a property to the player on it."""
        if person.money < 1000:
            print("Unfortunately, you lack the funds to develop this property. :(")
            return -1

        will_develop = input('Would you like to develop this property? (y/n)')

        if will_develop == 'y':

            dev = ''

            if person.money >= 7000:

                while dev != 'hos' and dev != 'bb' and dev != 'hot':
                    dev = input('Would you like to develop a hostel, B&B, or a hotel? (hos/bb/hot)')

                if dev == 'hos':
                    spot.develop(1000)
                    person.spend(1000)
                elif dev == 'bb':
                    spot.develop(3000)
                    person.spend(3000)
                elif dev == 'hot':
                    spot.develop(7000)
                    person.spend(7000)

            elif person.money >= 3000:

                while dev != 'hos' and dev != 'bb':
                    dev = input('Would you like to develop a hostel or a B & B? (hos/bb)')

                if dev == 'hos':
                    spot.develop(1000)
                    person.spend(1000)
                elif dev == 'bb':
                    spot.develop(3000)
                    person.spend(3000)

            else:
                while dev != 'y' and dev != 'n':
                    dev = input('Would you like to develop a hostel? (y/n)')
                if dev == 'y':
                    spot.develop(1000)
                    person.spend(1000)

                else:
                    print('Ok, \'till next time!')
                    return -1
            return 1
        return -1

    def check_loss(self, person: Player):
        """Checks if a player has lost the game!"""
        if person.money < 0:
            return True
        return False
