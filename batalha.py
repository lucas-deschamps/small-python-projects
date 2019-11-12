from sys import exit
from random import randint
from textwrap import dedent

# a small program I've written when I was conceptualizing how to develop a simple
# battle system class for implementation in another, much bigger project.

defeated = False

def display_hp(character):
    print("\nName: ", character['Name'], "\nHealth: ", character['Health'], '\n')

def damage_hp(attacker, target):
    damage = randint(1, 10)
    target['Health'] = target['Health'] - damage
    print(f"[{attacker['Name']} attacks {target['Name']} for {damage} damage.]")
    display_hp(target)

def defend(attacker, target):
    defend = randint(1, 4)
    target['Health'] = target['Health'] - defend
    print(f"\n{attacker['Name']} attacks {target['Name']} for {defend} damage.")
    display_hp(target)
    counter = randint(2, 4)
    attacker['Health'] -= counter
    print(f"{target['Name']} ripostes {attacker['Name']} for {counter} damage.")
    display_hp(attacker)

def player_death(character):
    if character['Health'] <= 0:
        print("You died.")
        print("Game over.")
        exit(0)


name = input("\nInput your name:\n> ")

my_character = {'Name' : name, 'Health' : 25}

display_hp(my_character)


print("A goblin holding a small dagger appears.")


goblin = {'Name' : 'Goblin', 'Health' : 30}

display_hp(goblin)


print("Goblin ambushes you...\n")

while goblin['Health'] >= 1:
    action = input(dedent('''What will you do?
* Attack
* Defend
* Run

> ''')).lower()

    if action == 'attack':
        print(f"You attack {goblin['Name']}...\n")
        damage_hp(my_character, goblin)
        damage_hp(goblin, my_character)

        player_death(my_character)

    elif action == 'defend':
        print("You assume a defensive stance.")
        defend(goblin, my_character)

        player_death(my_character)

    elif action == 'run':
        print("You attempt to escape the battle.")
        run = randint(0, 1)
        print(f"\n[Escape roll: {run}.]")
        print("\n[...]\n")

        if run == 1:
            print("You managed to escape the battle.")
            exit(0)

        else:
            print("You don't manage to get away.\n")

        damage_hp(goblin, my_character)

        player_death(my_character)

    else:
        print("Not a valid action.\n")

defeated = True

if defeated == True:
    print("Enemy defeated.")
    print("You were victorious. Game over.")
    exit(0)

elif defeated != True:
    print("You can't read this...")
