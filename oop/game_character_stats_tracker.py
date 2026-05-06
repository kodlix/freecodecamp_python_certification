'''
In this lab, you'll build a game character stats tracker. The program will allow you to create 
a character with specific attributes, update those attributes, and retrieve the current stats of the character.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.'''

class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self.health = 0
        elif new_health > 100:
            self.health = 100
        else:
            self._health = new_health

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            self.mana = 0
        elif new_mana > 50:
            self.mana = 50
        else:
            self._mana = new_mana

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level +=1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

game = GameCharacter('stevely')
game.mana = -44
print(game)