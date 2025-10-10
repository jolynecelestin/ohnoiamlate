rooms = {
        'Master bedroom': {'Up': 'Hallway 2'},
        'Hallway 2': {'Up': 'Closet', 'Down': 'Master bedroom', 'Right': 'Hallway 1', 'Left': 'Nursery'},
        'Nursery': {'Right': 'Hallway 2'},
        'Closet': {'Down': 'Hallway 2'},
        'Hallway 1': {'Up': 'Bathroom', 'Down': 'Living room', 'Right': 'Bedroom', 'Left': 'Hallway 2'},
        'Bathroom': {'Down': 'Hallway 1'},
        'Bedroom': {'Left': 'Hallway 1'},
        'Living room': {'Up': 'Hallway 1', 'Down': 'Entryway', 'Right': 'Dining room'},
        'Dining room': {'Down': 'Kitchen', 'Left': 'Living room'},
        'Kitchen': {'Up': 'Dining room', 'Left': 'Entryway'},
        'Entryway': {'Up': 'Living room', 'Down': 'Outside', 'Right': 'Kitchen', 'Left': 'Garage'},
        'Garage': {'Right': 'Entryway'},
        'Outside' : {}
}

time = 5

print('\nOh no you woke up late! Move between rooms using Up, Down, Right or Left. Time is running out!')

print("\n(Tip: if you want to quit the game at any point, type 'exit' and then press the [enter] key.)")

current_room = 'Master bedroom'

while True:
    print('\nTime remaining:',time,'minutes remaining')

    print(f"\nYou are in the {current_room}.")
    exits = rooms[current_room]
    print("\nExits:", ", ".join(exits.keys()) or "None")
    direction = input('Up, Down, Right or Left? ').strip().capitalize()
    time -= 1

    if time <  0 :
         print("\nYOU RAN OUT OF TIME, GAME OVER!.")
         break


    if direction in ('Exit', 'exit'):
        print('\nGame is ending now, hope you enjoyed it!')
        print('\nall done!\n')
        break
    
    if direction not in ('Up', 'Down', 'Right', 'Left'):
        print("\nPlease enter a valid direction (Up/Down/Right/Left).")
        continue
    elif direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
         print('\nOops, bumped into a wall.')

    if current_room == 'Outside':
        print('\nYou made it outside in time! YOU WIN!')
        print('\nall done!\n')
        break