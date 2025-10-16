import os
import platform

# --- Side functions---

#Clears screen at start of game
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

#Introduces player to game and objectives of the game. States basics on movement, how to collect items, and what to avoid to win.
def show_instructions():
    clear_screen()
    print("\nOh no you woke up late! Use 'Go (North, South, East or West)' to move between rooms.")
    print(f"Search rooms and type 'get (item)' to collect what you find! Collect all {len(original_items_remaining)} items and go outside to win")
    print("\n(Avoid finding and tripping over legos)")
    print("\n(Tip: type 'exit', 'quit', or 'q' anytime to quit.)")

# Displays what Current room you are in, directions you can go as 'Exits', Items remaining, current Inventory,and what item (if any) you see in the room.
def show_status(rooms, current_room, inventory):
    print ('\n-----------------------------------------------------------------------------------')
    print(f"\nYou are in the {current_room}.")
    local_exits = rooms[current_room]
    print("Exits:", ", ".join(local_exits.keys()) or "None")
    print("\nItems remaining:", items_remaining)
    print("Inventory:", inventory)
    room = room_items[current_room]
    if room:
        print(f"\nYou see a {', '.join(room)}...")
    else:
        print("\nYou see nothing...") 

#If an action you take starts with 'Get', then this will allow you to get an item in the room (if any) and add it to your inventory, afterwards removing it from items remaining as well as the respectives rooms item. If there is no item or you type in the wrong input, you will get the appropriate error.
def get_action(action, room_items, current_room, inventory):
    parts = action.split(maxsplit=1)
    if len(parts) == 2:
        item = parts[1].lower()
        if item in room_items[current_room]:
            if item not in inventory:
                inventory.append(item)
                items_remaining.remove(item)
                room_items[current_room].remove(item)
                print(f"\nYou picked up the {item}.")
            else:
                print(f"\nYou already have the {item}.")
        else:
            print(f"\nThere is no {item} here.")
    else:
        print("\nUsage: get (item)")

#If an action you take starts with 'Go', to either use go 'north/south/east/west'. 'go n/s/e/w' or 'go up/down/left/right' normalized so casing doesn't matter. If you don't type in a direction or type in the wrong direction in the wrong input, you will get the appropriate error. The action is split into parts, and that part is raw which is normalized in the direction.
def go_action(action, rooms):
    global current_room
    parts = action.split(maxsplit=1)
    if len(parts) == 1:
        print("\nUsage: go (direction)")
        return

    raw = parts[1].lower()
    direction = dir_aliases.get(raw, raw.title())
    exits_here = rooms[current_room]

    if direction in ('North', 'South', 'West', 'East'):
        if direction in exits_here:
            current_room = exits_here[direction]
            print(f"\nYou go {direction.lower()} into the {current_room}.")
        else:
            print("\nOops, bumped into a wall!")
    else:
        print("\nInvalid direction! Try North, South, West, or East.")
        

# --- Directions ---

dir_aliases = {
    'n': 'North', 'north': 'North', 'up': 'North',
    's': 'South', 'south': 'South', 'down': 'South',
    'e': 'East',  'east':  'East',  'right': 'East',
    'w': 'West',  'west':  'West',  'left':  'West'
}


# --- World map ---
rooms = {
    'Master bedroom': {'North': 'Hallway 2'},
    'Hallway 2': {'North': 'Closet', 'South': 'Master bedroom', 'East': 'Hallway 1', 'West': 'Nursery'},
    'Nursery': {'East': 'Hallway 2'},
    'Closet': {'South': 'Hallway 2'},
    'Hallway 1': {'North': 'Bathroom', 'South': 'Living room', 'East': 'Kids bedroom', 'West': 'Hallway 2'},
    'Bathroom': {'South': 'Hallway 1'},
    'Kids bedroom': {'West': 'Hallway 1'},
    'Living room': {'North': 'Hallway 1', 'South': 'Entryway', 'East': 'Dining room'},
    'Dining room': {'South': 'Kitchen', 'West': 'Living room'},
    'Kitchen': {'North': 'Dining room', 'West': 'Entryway'},
    'Entryway': {'North': 'Living room', 'South': 'Outside', 'East': 'Kitchen', 'West': 'Garage'},
    'Garage': {'East': 'Entryway'},
    'Outside': {}
}
# ---Items and Inventory---

original_room_items = {
    'Master bedroom': [],
    'Hallway 2':      [],
    'Nursery':        ['baby'],
    'Closet':         [],
    'Hallway 1':      [],
    'Bathroom':       ['diaper'],
    'Kids bedroom':        ['lego'],
    'Living room':    ['pacifier'],
    'Dining room':    [],
    'Kitchen':        ['bottle'],
    'Entryway':       ['car seat'],
    'Garage':         ['crib sheet'],
    'Outside':        ['car']
}

original_items_remaining = ['baby', 'diaper', 'pacifier', 'bottle', 'crib sheet', 'car seat']


# --- Game intro ---

room_items = {}         
items_remaining = []     
inventory = []      
current_room = 'Master bedroom'

# --- Replayability ---

#Resets Current room, and sets room items and items remaining before each start of the game.
def reset_state():
    global current_room, room_items, items_remaining, inventory
    current_room = 'Master bedroom'
    room_items = {k: v[:] for k, v in original_room_items.items()}
    items_remaining[:] = original_items_remaining[:]
    inventory.clear()

# --- Start game ---

#Organizes the functions into the main game, this inclues start and instructions, status, win and lose conditions, the main loop, exit conditions, and the get and go actions respectively.
def main():
    global current_room
    reset_state()
    show_instructions()


    # --- Status ---

    #Continues to run infinitely until game reaches win condition or lose condition then it breaks and prompts for a reset.
    while True:

        show_status(rooms, current_room, inventory)    
    


        # --- Win condition ---

        #Win condition is to go outside with no items remaining to collect
        if current_room == 'Outside':
            if not items_remaining:
                print("\nYou made it outside with everything! YOU WIN!\n")
                break
            else:
                print("\nYou reached outside, but you’re missing something!")
                missing = ", ".join(items_remaining)
                print(f"Missing: {missing}")
                current_room = 'Entryway'
                continue

        # --- Lose condition ---

        #Game ends if you run into the Villian (a single lego)
        if current_room == 'Kids bedroom':
                print("\n... but it was too late. you tripped over the single lego and broke your ankle!\n")
                print("\nOUCH! GAME OVER!!!\n")
                break
   
        # --- Loop ---

        #As long as you aren't outside or in the Kids bedroom, game continues to run. You are prompted for an action. 
        elif current_room != 'Outside':
            
            action = input("\nWhat would you like to do? (e.g., 'go North' or 'get Pacifier').\n\n(Tip: You can also type Up/Down/Left/Right or just 'north', 'go n', 'go up' etc.): ").strip().lower()
            
            # --- Exit check ---

            #Allows you at the prompt any action to exit the game safely 
            if action in ('exit', 'quit', 'q'):
                clear_screen()
                print("\nGame is ending now — hope you enjoyed it!")
                break

            # --- Get action ---

            #Runs get action
            if action.startswith('get'):
                get_action(action, room_items, current_room, inventory)
            
            # --- Move action ---


            #Runs go action
            elif action.startswith('go'):
                go_action(action, rooms)

            # --- Bare direction action ---

            #allows movement without go as long as movement is in dir_aliases
            elif action in dir_aliases:
                direction = dir_aliases[action]
                exits_here = rooms[current_room]
                if direction in exits_here:
                    current_room = exits_here[direction]
                    print(f"\nYou go {direction.lower()} into the {current_room}.")
                else:
                    print("\nOops, bumped into a wall!")
            else:
                print("\nInvalid command. Use 'get item' or 'go direction'.")

# --- Run game/Replay game ---

#Plays the main game. When break occurs in program, game prompts if user wants to replay. If yes the game clears and all settings reset before game plays again. If no, you safely leave the game.
if __name__ == "__main__":
    while True:
        main()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThanks for playing! all done!\n")
            break
        clear_screen() 
