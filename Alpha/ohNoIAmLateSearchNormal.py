import os
import platform


def clear_screen():
    # Works on Windows, macOS, and Linux
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


print('Oh no you woke up late! Search for everything you need before leaving. Time is running out!')

time = 30
print('\nTime remaining:',time,'minutes remaining')


items_remaining = ['baby', 'diapers', 'pacifier', 'bottle', 'clothes', 'car seat']
print('\nItems remaining:', items_remaining)

rooms_list = ['Master bedroom', 'Hallway 2', 'Nursery', 'Hallway 1','Bathroom', 'Bedroom', 'Living room', 'Dining room', 'Kitchen', 'Garage', 'Entryway', 'Outside']
print ('\nRooms:',rooms_list)

baby_bag = []

current_room = input('\nWhere are you? ').capitalize()

time -= 1

if current_room not in rooms_list:
    print("\nThat room doesn't exist! Please enter a valid room name.")
    current_room = input('Try again: ').lower()

while True:
    
    clear_screen()
    
    if time <  0 :
         print("\nYOU RAN OUT OF TIME, GAME OVER!.")
         break
    
    if current_room == 'Outside':
        if len(baby_bag) == 6:
            print('\nYay! You got everything, all done!')
            break
        else:
            print("\nYou don't have everything, you need to keep looking!")
            current_room = 'Entryway'
            continue
        
    
    print('\nTime remaining:',time,'minutes remaining')
    
    print(f'\n(You are in the {current_room})')
    
    
    search = input('\nWould you like to search the room?').lower()
    
    clear_screen()
    
    if search == 'yes':
        print('You are searching and found…')

        if current_room == 'Master bedroom':
            print('…nothing.')
            time -= 2

        elif current_room == 'Hallway 2':
            print('…nothing.')
            time -= 2

        elif current_room == 'Nursery':
            print('…a baby!')
            baby_bag.append('baby')
            items_remaining.remove('baby')
            time -= 1
            
        elif current_room == 'Hallway 1':
            print('…nothing.')
            time -= 2

        elif current_room == 'Bathroom':
            print('…diapers!')
            baby_bag.append('diapers')
            items_remaining.remove('diapers')
            time -= 1
            
        elif current_room == 'Bedroom':
            print('…nothing.')
            time -= 2

        elif current_room == 'Living room':
            print('…a pacifier!')
            baby_bag.append('pacifier')
            items_remaining.remove('pacifier')
            time -= 1

        elif current_room == 'Dining room':
            print('…nothing.')
            time -= 2

        elif current_room == 'Kitchen':
            print('…a bottle!')
            baby_bag.append('bottle')
            items_remaining.remove('bottle')
            time -= 1

        elif current_room == 'Garage':
            print('…clothes!')
            baby_bag.append('clothes')
            items_remaining.remove('clothes')
            time -= 1

        elif current_room == 'Entryway':
            print('…a car seat!')
            baby_bag.append('car seat')
            items_remaining.remove('car seat')
            time -= 1

        else:
            print('Please enter a proper room name.')
            time -= 1
            

    elif search == 'no':
        print('Okay, moving on.')

    else:
        print("Please answer 'yes' or 'no'.")
       
    if time <  0 :
         print("\nYOU RAN OUT OF TIME, GAME OVER!.")
         break
    
    print('\nTime remaining:',time,'minutes remaining')
    print('\nBaby bag:', baby_bag)
    print('Items remaining:', items_remaining)
    print ('\nRooms:',rooms_list)
    current_room = input('\nWhich room would you like to go to next? ').capitalize()
    time -= 1