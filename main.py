from random import randint
from objects import Player, Weapon, Armor, Shield, Food, Monster
from words import randomAdj

print("Donegeon")
print("By Joel Newswanger")


def event():
    what = randint(0, 6)
    inside = randint(0, 5)
    if what == 3:
        open_it = input("An " + randomAdj() +
                   ' human is sitting in the middle of the room. Greet them? y/n: ')
        if open_it == 'y':
            print("They are not ready.")
        else:
            print("You avoid the man's friendly smile, and leave the room quickly.")
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
        if open_it != "y":
            if what == 0 or what == 4:
                print("You pass by the chest. There may be something dangerous in there, after all.")
            elif what == 1 or what == 5:
                print("You leave the door closed. A monster may have lurked behind it.")
        else:
            if inside == 0:
                new_item = Weapon(iname)
                print('The', new_item.name, new_item.power[0], new_item.power[1], "is a weapon.")
            elif inside == 1:
                new_item = Armor(iname)
                print('The', new_item.name, new_item.defence, "is armor.")
            elif inside == 2:
                new_item = Shield(iname)
                print('The', new_item.name, new_item.defence, "is a shield.")
            elif inside == 3:
                new_item = Food(iname)
                print('The', new_item.name, new_item.hp, "is food.")
            elif inside == 4:
                monster = Monster(iname)
                print('The', monster.name, 'is a monster with attack (', monster.power, '), defence (', monster.defence,
                      '), and health (', monster.hp, ').')


while True:
    print('Options (shortcuts):')
    start = input("play (p), highscores (h), settings (s), quit (q)? : ")
    if start == "play" or start == "p":
        player = Player()
        print("Welcome to Donegeon, " + player.name + "!")
        print("It's dangerous to go alone! Take this basic sword (10-50).")
        print("Entering the Donegeon!")
        while not player.dead:
            action = input('status (s), inventory (i), equip (eq), eat, or continue (c)? : ')
            if action == 'status' or action == 's':
                player.status()
            if action == 'inventory' or action == 'i':
                player.chkinv()
            if action == 'equip' or action == 'eq':
                player.equip()
            if action == 'eat':
                player.eat()
            if action == 'continue' or action == 'c':
                event()
            else:
                    print('Invalid entry.')
    elif start == "highscores" or start == "h":
        print("Can't do that yet.")
    elif start == "settings" or start == "s":
        print("Can't do that yet.")
    elif start == "quit" or start == "q":
        break
    else:
        print("Invalid entry.")

print("Thank you for playing Donegeon.")
print("This game was created by Joel Newswanger.")