from random import randint
from objects import Player, Weapon, Armor, Shield, Food, Monster, Quest, Wizard
from words import randomAdj

print("Donegeon")
print("By Joel Newswanger")


def event():
    what = randint(0, 6)
    inside = randint(0, 4)
    if what == 3:
        if randint(0, 2) == 0:
            npc = Quest()
        else:
            npc = Wizard()
        open_it = input("A " + npc.title + " " + npc.descriptor +
                   ' is sitting in the middle of the room. Greet them? y/n: ')
        if open_it == 'y':
            npc.greet(player)
        else:
            print("You avoid the " + npc.descriptor + "'s friendly smile, and leave the room quickly.")
    else:
        if what == 0 or what == 4:
            open_it = input('Here is a chest! Open it? y/n: ')
            if open_it == "y":
                iname = input("You throw the chest open! What's this?: ")
        elif what == 1 or what == 5:
            open_it = input("There's a door in the corner. Open it? y/n: ")
            if open_it == "y":
                iname = input("You kick down the door with a shout! What's that behind it?: ")
        elif what == 2 or what == 6:
            open_it = 'y'
            print("Some rocks fall down behind you, you're trapped!")
            iname = input("Something lands on the ground in front of you! What is it?: ")
        if open_it == "n":
            if what == 0 or what == 4:
                print("You pass by the chest. There may be something dangerous in there, after all.")
            elif what == 1 or what == 5:
                print("You leave the door closed. A monster may have lurked behind it.")
        elif open_it == "y":
            if inside == 0:
                new_item = Weapon(iname)
                player.weapons.append(new_item)
                print('The', new_item.name, new_item.power0, new_item.power1, "is a weapon.")
            elif inside == 1:
                new_item = Armor(iname)
                player.armors.append(new_item)
                print('The', new_item.name, new_item.defence, "is armor.")
            elif inside == 2:
                new_item = Shield(iname)
                player.shields.append(new_item)
                print('The', new_item.name, new_item.defence, "is a shield.")
            elif inside == 3:
                new_item = Food(iname)
                player.foods.append(new_item)
                print('The', new_item.name, new_item.hp, "is food.")
            elif inside == 4:
                monster = Monster(iname)
                print('The', monster.name, 'is a monster with attack (', monster.power0, ",", monster.power1, '),'
                      ' defence (', monster.defence, '), and health (', monster.hp, ').')
                monster.fight(player)
        else:
            print("You got confused and ran away.")


corpses = []

while True:
    print('Options (shortcuts):')
    start = input("play (p), highscores (h), settings (s), quit (q)? : ")
    if start == "play" or start == "p":
        player = Player()
        print("Welcome to Donegeon, " + player.name + "!")
        print("It's dangerous to go alone! Take this basic sword (10-50).")
        print("Entering the Donegeon!")
        while not player.dead:
            action = input('status (s), inventory (i), equip (eq), magic (m), eat, or continue (c)? : ')
            if action == 'status' or action == 's':
                player.status()
            elif action == 'inventory' or action == 'i':
                player.chkinv()
            elif action == 'equip' or action == 'eq':
                player.equip()
            elif action == 'magic' or action == 'm':
                if not player.wizard:
                    print("You're pretty sure you can't do magic.")
                elif player.wizard:
                    player.magic()
            elif action == 'eat':
                player.eat()
            elif action == 'continue' or action == 'c':
                player.rooms_cleared += 1
                event()
            else:
                    print('Invalid entry.')
        corpses.append(player)
    elif start == "highscores" or start == "h":
        for corpse in corpses:
            print(corpse.name + " achieved " + str(corpse.fame) + " fame, while traversing " + str(corpse.rooms_cleared)
                  + " rooms of the Donegeon.")
    elif start == "settings" or start == "s":
        print("There are no settings.")
    elif start == "quit" or start == "q":
        break
    else:
        print("Invalid entry.")

print("Thank you for playing Donegeon.")
print("This game was created by Joel Newswanger.")