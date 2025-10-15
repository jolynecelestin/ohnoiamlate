import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
# --- World Map ---
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
    'Outside': {}
}
# ---Items and Inventory---

room_items = {
    'Master bedroom': [],
    'Hallway 2':      [],
    'Nursery':        ['baby'],
    'Closet':         [],
    'Hallway 1':      [],
    'Bathroom':       ['diapers'],
    'Bedroom':        [],
    'Living room':    ['pacifier'],
    'Dining room':    [],
    'Kitchen':        ['bottle'],
    'Entryway':       ['car seat'],
    'Garage':         ['clothes'],
    'Outside':        []
}

items_remaining = ['baby', 'diapers', 'pacifier', 'bottle', 'clothes', 'car seat']
baby_bag = []

# --- Game intro ---
clear_screen()
print('\nOh no you woke up late! Move between rooms using North, South, East or West. Time is running out!')
print('Search rooms and type "get (item)" to collect what you find!')
print("\n(Tip: type 'exit', 'quit', or 'q' anytime to quit.)")

current_room = 'Master bedroom'


# --- Intro Loop ---
while True:
    print ('\n-----------------------------------------------------------------------------------')
    print(f"\nYou are in the {current_room}.")
    exits = rooms[current_room]
    print("Exits:", ", ".join(exits.keys()) or "None")
    print('\nItems remaining:', items_remaining)
    print('Inventory:', baby_bag)
    

    # --- Win condition ---
    if current_room == 'Outside':
        if len(baby_bag) == 6:
            print('\nYou made it outside with everything! YOU WIN!\n')
            print('\nall done!\n')
            break
        else:
            print("\nYou reached outside, but you’re missing something!")
            missing = ", ".join(items_remaining)
            print(f"Missing: {missing}")
            current_room = 'Entryway'
            continue

   
    elif current_room != 'Outside':
        action = input("\nWhat would you like to do? (e.g., 'go north' or 'get item'): ").strip().lower()
        
   
        # --- Exit check ---
        if action in ('exit', 'quit', 'q'):
            clear_screen()
            print('\nGame is ending now — hope you enjoyed it!')
            print('\nall done!\n')
            break

        # --- Get action ---
        if action.startswith('get'):
            parts = action.split(maxsplit=1)
            if len(parts) == 2:
                item = parts[1].lower()
                if item in room_items[current_room]:
                    if item not in baby_bag:
                        baby_bag.append(item)
                        items_remaining.remove(item)
                        room_items[current_room].remove(item)
                        print(f"\nYou picked up the {item}.")
                    else:
                        print(f"\nYou already have the {item}.")
                else:
                    print(f"\nThere is no {item} here.")
            else:
                print("\nUsage: get (item)")

        # --- Move ---
        elif action.startswith('go'):
            parts = action.split(maxsplit=1)
            if len(parts) == 2:
                direction = parts[1].lower()
                if direction.title() in ('North', 'South', 'East', 'West'):
                    if direction.title() in exits:
                        current_room = exits[direction.title()]
                    else:
                        print("\nOops, bumped into a wall!")
                else:
                    print("\nInvalid direction! Try North, South, East, or West.")
            else:
                print("\nInvalid command. Use 'get item' or 'go direction'.")
        else:
            print("\nInvalid command. Use 'get item' or 'go direction'.")
        
              
