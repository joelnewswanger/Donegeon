from random import randint
from words import randomAdj


class Item:
    name = ""
    power = [0, 0]
    defence = 0
    hp = 0

    def __init__(self, name_in):
        self.power[0] = randint(1, 100)
        self.power[1] = self.power[0] + randint(1, 100)
        self.defence = randint(1, 60)
        self.hp = randint(10, 60)
        self.name = randomAdj() + " " + name_in


class Weapon(Item):
    def __init__(self, name_in):
        super().__init__(name_in)
        if ((self.power[0] + self.power[1]) / 2) > 50:
            self.name = randomAdj() + " " + self.name
            if ((self.power[0] + self.power[1]) / 2) > 100:
                self.name = randomAdj() + " " + self.name


class Armor(Item):
    def __init__(self, name_in):
        super().__init__(name_in)
        if self.defence > 20:
            self.name = randomAdj() + " " + self.name
            if self.defence > 40:
                self.name = randomAdj() + " " + self.name


class Shield(Armor):
    shield = True


class Food(Item):
    def __init__(self, name_in):
        super().__init__(name_in)
        if self.hp > 20:
            self.name = randomAdj() + " " + self.name
            if self.hp > 40:
                self.name = randomAdj() + " " + self.name


class Monster(Item):
    level = 0

    def __init__(self, name_in):
        super().__init__(name_in)
        self.level = ((self.power[0] + self.power[1]) / 2) + self.defence + self.hp
        if self.level > 100:
            self.name = randomAdj() + " " + self.name
            self.hp = self.hp * 2
            if self.level > 200:
                self.name = randomAdj() + " " + self.name
                self.hp = self.hp * 2


class Player:
    name = "Player"
    weapon = Weapon("Basic Sword")
    armor = Armor("shirt")
    shield = Shield("No Shield")
    amulet = 'natural'
    health = 200
    dead = False
    fame = 0
    weapons = []
    armors = []
    shields = []
    foods = []
    inventory = [weapons, armors, shields, foods]

    def __init__(self):
        self.name = input("What is your name?: ") + " the " + randomAdj()
        self.weapon.name = "basic sword"
        self.weapon.power = [10, 50]
        self.armor.defence = 10
        self.shield.name = "no shield"
        self.shield.defence = 0
        self.weapons.append(self.weapon)

    def status(self):
        print('You have', self.health, ' hitpoints.')
        print('The name ', self.name, 'has approximately ', self.fame, ' fame on the Bendrojh-Fimblston scale.')
        print('You are wielding a', self.weapon.name, self.weapon.power[1], self.weapon.power[0])
        print('You are wearing a', self.armor.name, self.armor.defence, ' and defending yourself with a',
              self.shield.name, self.shield.defence, ".")

    def chkinv(self):  # Check inventory
        print('weapons: ', self.weapons)
        print('armors: ', self.armors)
        print('shields: ', self.shields)
        print('foods: ', self.foods)

    def equip(self):
        print("not implemented")

    def eat(self):
        print("not implemented")

    def death(self):  # In event you are defeated in battle, checks for food in backpack, else game over
        totfood = 0
        for key in self.foods:
            totfood += self.foods[key].hp
        if 0 - totfood < self.health:
            print('You will survive if you eat something.')
        else:
            self.dead = True
            print('You died wielding', self.weapon.name, ', wearing a ', self.armor.name, ', and ', self.shield.name, '. ')
            print('The name of ', self.name, ' had ', self.fame, ' fame on the Bendrojh-Fimblston scale.')
            print('Game Over.')


