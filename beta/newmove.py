import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

rooms = {
        'Master bedroom': {'North': 'Hallway 2'},
        'Hallway 2': {'North': 'Closet', 'South': 'Master bedroom', 'East': 'Hallway 1', 'West': 'Nursery'},
        'Nursery': {'East': 'Hallway 2'},
        'Closet': {'South': 'Hallway 2'},
        'Hallway 1': {'North': 'Bathroom', 'South': 'Living room', 'East': 'Bedroom', 'West': 'Hallway 2'},
        'Bathroom': {'South': 'Hallway 1'},
        'Bedroom': {'West': 'Hallway 1'},
        'Living room': {'North': 'Hallway 1', 'South': 'Entryway', 'East': 'Dining room'},
        'Dining room': {'South': 'Kitchen', 'West': 'Living room'},
        'Kitchen': {'North': 'Dining room', 'West': 'Entryway'},
        'Entryway': {'North': 'Living room', 'South': 'Outside', 'East': 'Kitchen', 'West': 'Garage'},
        'Garage': {'East': 'Entryway'},
        'Outside' : {}
}

time = 30

clear_screen()


print('\nOh no you woke up late! Move between rooms using North, South, East or West. Time is running out!')

print("\n(Tip: if you want to quit the game at any point, type 'exit' and then press the [enter] key.)")

current_room = 'Master bedroom'

while True:
    print('\nTime remaining:',time,'minutes remaining')

    print(f"\nYou are in the {current_room}.")
    exits = rooms[current_room]
    print("\nExits:", ", ".join(exits.keys()) or "None")
    direction = input('North, South, East or West? ').strip().capitalize()
    time -= 1
    clear_screen()

    if time <  0 :
         print("\nYOU RAN OUT OF TIME, GAME OVER!.")
         break

    if direction in ('Exit', 'exit'):
        print('\nGame is ending now, hope you enjoyed it!')
        print('\nall done!\n')
        break
    
    if direction not in ('North', 'South', 'East', 'West'):
        print("\nPlease enter a valid direction (North/South/East/West).")
        continue
    elif direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
         print('\nOops, bumped into a wall.')

    if current_room == 'Outside':
        print('\nYou made it outside in time! YOU WIN!')
        print('\nall done!\n')
        break