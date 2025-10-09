import sys
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def ask(prompt):
    user_input = input(prompt).strip().lower()
    if user_input in ['quit']:
        print("\nall done!")
        sys.exit()
    return user_input

clear_screen()
print("Oh no you woke up late! Move between rooms using North, South, East or West. Time is running out!")

time = 30

current_room = 'Master Bedroom'

while True:
    print('\nTime remaining:',time,'minutes remaining')
    
    print(f"\nYou are in {current_room}.")
    direction = ask('North, South, East or West? ').strip().lower()
    clear_screen()
    
    if time <=  0 :
         print("\nYOU RAN OUT OF TIME, GAME OVER!.")
         break
     
    time -=1
 
    if current_room == 'Master Bedroom':
        if direction == 'north':
            current_room = 'Hallway 2'
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Hallway 2':
        if direction == 'south':
            current_room = 'Master Bedroom'
        elif direction == 'east':
            current_room = 'Hallway 1'
        elif direction == 'west':
            current_room = 'Nursery'
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Nursery':
        if direction == 'east':
            current_room = 'Hallway 2'     
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Hallway 1':
        if direction == 'north':
            current_room = 'Bathroom'
        elif direction == 'south':
            current_room = 'Living Room'
        elif direction == 'east':
            current_room = 'Bedroom'
        elif direction == 'west':
            current_room = 'Hallway 2'
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Bathroom':
        if direction == 'south':
            current_room = 'Hallway 1'
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Bedroom':
        if direction == 'west':
            current_room = 'Hallway 1'
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Living Room':
        if direction == 'north':
            current_room = 'Hallway 1'
        elif direction == 'south':
            current_room = 'Entryway'
        elif direction == 'east':
            current_room = 'Dining Room'
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Dining Room':
        if direction == 'south':
            current_room = 'Kitchen'
        elif direction == 'west':
            current_room = 'Living Room'
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Kitchen':
        if direction == 'north':
            current_room = 'Dining Room'
        elif direction == 'west':
            current_room = 'Entryway'
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Garage':
        if direction == 'east':
            current_room = 'Entryway'
        else:
            print('\nOops, bumped into a wall.')
            continue

    elif current_room == 'Entryway':
        if direction == 'north':
            current_room = 'Living Room'
        elif direction == 'south':
            current_room = 'Outside'
        elif direction == 'east':
            current_room = 'Kitchen'
        elif direction == 'west':
            current_room = 'Garage'
        else:
            print('\nOops, bumped into a wall.')
            continue

    else:
        break

    if current_room == 'Outside':
        print('You made it outside in time! all done!')
        break