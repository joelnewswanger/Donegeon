from random import randint
from words import randomAdj


class Item:
    name = ""
    power0 = 0
    power1 = 1
    defence = 0
    hp = 0

    def __init__(self, name_in):
        self.power0 = randint(1, 100)
        self.power1 = self.power0 + randint(1, 100)
        self.defence = randint(1, 60)
        self.hp = randint(10, 60)
        self.name = randomAdj() + " " + name_in


class Weapon(Item):
    itemtype = "weapon"
    def __init__(self, name_in):
        super().__init__(name_in)
        if ((self.power0 + self.power1) / 2) > 50:
            self.name = randomAdj() + " " + self.name
            if ((self.power0 + self.power1) / 2) > 100:
                self.name = randomAdj() + " " + self.name


class Armor(Item):
    itemtype = "armor"
    def __init__(self, name_in):
        super().__init__(name_in)
        if self.defence > 20:
            self.name = randomAdj() + " " + self.name
            if self.defence > 40:
                self.name = randomAdj() + " " + self.name


class Shield(Armor):
    itemtype = "shield"


class Food(Item):
    def __init__(self, name_in):
        super().__init__(name_in)
        if self.hp > 20:
            self.name = randomAdj() + " " + self.name
            if self.hp > 40:
                self.name = randomAdj() + " " + self.name


class Monster(Item):
    level = 0
    dead = False

    def __init__(self, name_in):
        super().__init__(name_in)
        self.level = ((self.power0 + self.power1) / 2) + self.defence + self.hp
        if self.level > 100:
            self.name = randomAdj() + " " + self.name
            self.hp = self.hp * 2
            if self.level > 200:
                self.name = randomAdj() + " " + self.name
                self.hp = self.hp * 2

    def fight(self, player):
        cont = input('Are you prepared to fight the ' + self.name + '? y/n/s: ')
        if cont == "s" or cont == "status":
            player.status()
            self.fight(player)
        elif cont == "y":
            defeat = False
            while not defeat and not self.dead:
                playerDmg = randint(player.weapon.power0, player.weapon.power1) - self.defence
                if playerDmg > 0:
                    self.hp -= playerDmg
                print("You do", playerDmg, "damage. The", self.name, "has", self.hp, "health left.")
                if self.hp > 0:
                    monsteratk = randint(self.power0, self.power1)
                    pd = player.armor.defence + player.shield.defence
                    print("Monster attacks" + str(monsteratk) + ". Player defends " + str(pd))
                    monsterDmg = monsteratk - pd
                    if monsterDmg > 0:
                        player.health -= monsterDmg
                    print(self.name, "does", monsterDmg, "damage. You have", player.health, "health left.")
                else:
                    self.dead = True
                    print("You have slain the", self.name, "with your", player.weapon.name, ", while wearing a",
                          player.armor.name, "\n and defending yourself with a", player.shield.name, ".")
                    player.fame = player.fame + self.level
                    print("Your heroic deed gained you", self.level, "fame. The name of", player.name, "is now at",
                          player.fame, "on the Bendrojh-Fimblston scale!")
                    return True
                if player.health < 1:
                    defeat = True
                    print("The", self.name, "has defeated you.")
                    player.death()
        else:
            cowardice = 270 - self.level
            if cowardice > 0:
                player.fame -= cowardice
                print("You flee from the " + self.name + ".")
                print("Your reputation is marred by your cowardly action. You lose " + str(cowardice) + " fame.")
                luck = randint(0,4)
                if luck == 0:
                    dmg = (randint(self.power0, self.power1) - player.armor.defence - player.shield.defence)
                    if dmg > 0:
                        player.health -= dmg
                        print("The " + self.name + " takes the opportunity to attack. You lose " + str(dmg) + " health.")
                        if player.health < 1:
                            player.death()


class Player:
    name = "Player"
    weapon = Weapon("Basic Sword")
    armor = Armor("shirt")
    shield = Shield("No Shield")
    amulet = 'natural'
    health = 200
    dead = False
    wizard = False
    fame = 0
    weapons = []
    armors = []
    shields = []
    foods = []
    fessence = 0
    wessence = 0
    eessence = 0

    def __init__(self):
        self.name = input("What is your name?: ") + " the " + randomAdj()
        self.weapon.name = "basic sword"
        self.weapon.power0 = 10
        self.weapon.power1 = 50
        self.armor.defence = 10
        self.armor.name = "shirt"
        self.shield.name = "no shield"
        self.shield.defence = 0
        self.weapons = []
        self.armors = []
        self.shields = []
        self.foods = []

    def status(self):
        print('You have', self.health, 'hitpoints.')
        print('The name', self.name, 'has approximately', self.fame, 'fame on the Bendrojh-Fimblston scale.')
        print('You are wielding a', self.weapon.name, self.weapon.power0, "-", self.weapon.power1)
        print('You are wearing a', self.armor.name, self.armor.defence, 'and defending yourself with a',
              self.shield.name, self.shield.defence, ".")

    def chkinv(self):  # Check inventory
        list_weapons = ""
        for item in self.weapons:
            list_weapons = list_weapons + item.name + "(" + str(item.power0) + "," + str(item.power1) + "), "
        list_weapons = list_weapons[:-2] + "."
        print('weapons: ', list_weapons)
        list_armors = ""
        for item in self.armors:
            list_armors = list_armors + item.name + "(" + str(item.defence) + "), "
        list_armors = list_armors[:-2] + "."
        print('armors: ', list_armors)
        list_shields = ""
        for item in self.shields:
            list_shields = list_shields + item.name + "(" + str(item.defence) + "), "
        list_shields = list_shields[:-2] + "."
        print('shields: ', list_shields)
        list_foods = ""
        for item in self.foods:
            list_foods = list_foods + item.name + "(" + str(item.hp) + "), "
        list_foods = list_foods[:-2] + "."
        print('foods: ', list_foods)

    def haveitem(self, name):
        for weapon in self.weapons:
            if weapon.name == name:
                return weapon
        for armor in self.armors:
            if armor.name == name:
                return armor
        for shield in self.shields:
            if shield.name == name:
                return shield
        for food in self.foods:
            if food.name == name:
                return food
        print("Could not find " + name)
        return False

    def equip(self):
        equipment = input("What would you like to equip? (Or say 'best'): ")
        found = False
        if equipment == "best":
            found = True
            spec = input("Choose: all, weapon, armor, shield: ")
            if spec == "all" or spec == "weapon":
                best = self.weapon
                for w in self.weapons:
                    if ((w.power0 + w.power1)/2) > ((best.power0 + best.power1)/2):
                        best = w
                self.weapon = best
                print('You have equipped the', self.weapon.name, self.weapon.power0, '-', self.weapon.power1,
                      "as a weapon.")
            if spec == "all" or spec == "armor":
                best = self.armor
                for a in self.armors:
                    if a.defence > best.defence:
                        best = a
                self.armor = best
                print('You have equipped the', self.armor.name, self.armor.defence, "as armor.")
            if spec == "all" or spec == "shield":
                best = self.shield
                for s in self.shields:
                    if s.defence > best.defence:
                        best = s
                self.shield = best
                print("You have equipped the", self.shield.name, self.shield.defence, "as shield.")
        else:
            item = self.haveitem(equipment)
            if not item:
                return False
            if item.itemtype == "weapon":
                self.weapon = item
            elif item.itemtype == "armor":
                self.armor = item
            elif item.itemtype == "shield":
                self.shield = item
            else:
                print("You can't wear that.")
            print("You equip the " + item.name + " as your " + item.itemtype + ".")

    def magic(self):
        print("You have " + str(self.fessence) + " fire essence, " + str(self.wessence) + " water essence, and " +
              str(self.eessence) + " earth essence.")
        choice = input("Extract essence or cast spell? e/s : ")
        if choice == "e":
            extract = input("What do you extract the essence from? For all except equipped, say 'all'. : ")
            if extract == 'all':
                fe = 0
                we = 0
                ee = 0
                for w in self.weapons:
                    if w.name != self.weapon.name:
                        fe += ((w.power0 + w.power1)*0.1)
                self.weapons = [self.weapon]
                for a in self.armors:
                    if a.name != self.armor.name:
                        we += (a.defence * 0.1)
                self.armors = [self.armor]
                for s in self.shields:
                    if s.name != self.armor.name:
                        ee += (s.defence * 0.1)
                self.shields = [self.shield]
                self.fessence += fe
                self.wessence += we
                self.eessence += ee
                print("You extract from all the items you are not using and obtain " + str(fe) + " fire essence, " +
                      str(we) + " water essence, and " + str(ee) + " earth essence.")
        elif choice == "s":
            cast = input("Cast: fire (f), water (w), or earth (e)? : ")
            if cast == "fire" or cast == "f":
                target = input("Warmth blooms within you. Focus on your weapon? y/n: ")
                if target == "y":
                    percentage = randint(1,99)
                    a0 = self.fessence * (percentage/100)
                    a1 = self.fessence - a0
                    self.weapon.power0 += a0
                    self.weapon.power1 += a1
                    self.fessence = 0
                    print("You channel the fire essence into your " + self.weapon.name + ", increasing its power by ("
                          + str(a0) + ", " + str(a1) + ").")
            elif cast == "water" or cast == "w":
                target = input("A surge of power flows through you. Focus on your armor? y/n: ")
                if target == "y":
                    self.armor.defence += self.wessence
                    print("You channel the water essence into your " + self.armor.name + ", increasing its defence by "
                          + str(self.wessence) + ".")
                    self.wessence = 0
            elif cast == "earth" or cast == "e":
                target = input("A great power weighs on you. Focus on your shield? y/n: ")
                if target == "y":
                    self.shield.defence += self.eessence
                    print("You channel the earth essence into your " + self.shield.name + " increasing its defence by "
                          + str(self.eessence) + ".")
                    self.eessence = 0

    def eat(self):
        target = input("What do you want to eat? Or say 'all'. : ")
        if target == 'all':
            sumhp = 0
            for food in self.foods:
                sumhp = sumhp + food.hp
            self.foods = []
            self.health = self.health + sumhp
            print("You eat all the food you have and regain " + str(sumhp) + " health.")
        else:
            food = self.haveitem(target)
            if not food:
                return False
            else:
                self.health = self.health + food.hp
                self.foods.pop(self.foods.index(food))
                print("You eat the " + food.name + " and regain " + str(food.hp) + " health.")

    def death(self):  # In event you are defeated in battle, checks for food in backpack, else game over
        totfood = 0
        for key in self.foods:
            totfood += key.hp
        if 0 - totfood < self.health:
            print('You will survive if you eat something.')
        else:
            self.dead = True
            print('You died wielding', self.weapon.name, ', wearing a ', self.armor.name, ', and ', self.shield.name,
                  '. ')
            print('The name of ', self.name, ' had ', self.fame, ' fame on the Bendrojh-Fimblston scale.')
            print('Game Over.')


class NPC:
    descriptor = "man"
    title = "old"
    age = 3
    gender = 1

    def __init__(self):
        descs = [["girl", "young lady", "woman", "old woman"], ["boy", "young lad", "man", "old man"]]
        self.title = randomAdj()
        self.gender = randint(0, 1)
        self.age = randint(0, 3)
        self.descriptor = descs[self.gender][self.age]


class Quest(NPC):
    def __init__(self):
        super().__init__()

    def greet(self, player):
        print("'" + self.descriptor + "': I need your help adventurer! There is a powerful monster blocking my path.")
        ready = input("Can you defeat it? y/n: ")
        if ready == "y":
            print("You follow the path to where the " + self.descriptor + " directed you.")
            bossname = input("What could that be?: ")
            boss = Monster("Boss")
            boss.name = "epically" + " " + randomAdj() + " " + bossname
            lucky = randint(0, 30)
            boss.power = [90 - lucky, 130 + lucky]
            boss.hp = 250
            boss.defence = 90
            boss.level = 500
            print("The " + boss.name + " is a boss monster with attack (", boss.power, '), defence (', boss.defence,
                  '), and health (', boss.hp, ').')
            if boss.fight(player):
                print("The " + self.descriptor + " thanks you for your heroism and hurries away.")
        else:
            print("I don't blame you, kid. I turned and ran myself!")


class Wizard(NPC):
    def __init__(self):
        super().__init__()

    def greet(self, player):
        if player.fame < 750:
            print('Greetings stranger. You must be new to these parts, I have not heard tell of your adventures.')
            print('I am here to teach great heroes the ancient magic.')
            print("That way when they emerge from Donegeon, I can take partial credit for all their great deeds! HEHEHE!")
            print('The mysterious stranger has disappeared...')
        else:
            print("'Greetings ", player.name, "! I have heard of your great heroism in Donegeon!'")
            print("'I can mentor you in the ways of ancient magic, so that nothing may stand in your way!'")
            response = input('Begin lesson? (y/n): ')
            if response == "y":
                print("'As you may have noticed, Donegeon contains some unusual things.'")
                print("'This is because of a deep " + randomAdj() + " magic that was spilled here.'")
                attention = input("The " + self.descriptor + " describes the nature of the magic at length. Pay attention? (y/n): ")
                print("'...in the same way the magic naturally imbues items, we can manipulate it to create spells.'")
                print("'First extract the essence from an item that has been imbued in the Donegeon. Like this.'")
                focus = input("'Now I will teach you to create a spell.' Focus? y/n: ")
                print("The essence becomes a " + randomAdj() + " fireball, which explodes against the far wall.")
                print("You're pretty sure you figured out how it was done.")
                player.wizard = True
            else:
                print("'Very well. Return when you are ready to learn.")
