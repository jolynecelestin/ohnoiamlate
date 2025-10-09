print('Oh no you woke up late! Search for everything you need before leaving. Time is running out!')

items_remaining = ['baby', 'diapers', 'pacifier', 'bottle', 'clothes', 'car seat']
print('\nItems remaining...:', items_remaining)

rooms_list = ['Master bedroom', 'Hallway 2', 'Nursery', 'Hallway 1','Bathroom', 'Bedroom', 'Living room', 'Dining room', 'Kitchen', 'Laundry room', 'Entryway', 'Outside']
print ('\nRooms:',rooms_list)

baby_bag = []

current_room = input('\nWhere are you? ').capitalize()

if current_room not in rooms_list:
    print("\nThat room doesn't exist! Please enter a valid room name.")
    current_room = input('Try again: ').lower()

while True:
    
    if current_room == 'Outside':
        if len(baby_bag) == 6:
            print('\nYay! You got everything, all done!')
            break
        else:
            print("\nYou don't have everything, you need to keep looking!")
            current_room = 'Entryway'
            continue
    
    
    print(f'\n(You are in the {current_room})')
    
    search = input('\nWould you like to search the room?').lower()

    if search == 'yes':
        print('You are searching and found…')

        if current_room == 'Master bedroom':
            print('…nothing.')

        elif current_room == 'Hallway 2':
            print('…nothing.')

        elif current_room == 'Nursery':
            print('…a baby!')
            baby_bag.append('baby')
            items_remaining.remove('baby')

        elif current_room == 'Hallway 1':
            print('…nothing.')

        elif current_room == 'Bathroom':
            print('…diapers!')
            baby_bag.append('diapers')
            items_remaining.remove('diapers')

        elif current_room == 'Bedroom':
            print('…nothing.')

        elif current_room == 'Living room':
            print('…a pacifier!')
            baby_bag.append('pacifier')
            items_remaining.remove('pacifier')

        elif current_room == 'Dining room':
            print('…nothing.')

        elif current_room == 'Kitchen':
            print('…a bottle!')
            baby_bag.append('bottle')
            items_remaining.remove('bottle')

        elif current_room == 'Laundry room':
            print('…clothes!')
            baby_bag.append('clothes')
            items_remaining.remove('clothes')

        elif current_room == 'Entryway':
            print('…a car seat!')
            baby_bag.append('car seat')
            items_remaining.remove('car seat')

        else:
            print('Please enter a proper room name.')
            

    elif search == 'no':
        print('Okay, moving on.')

    else:
        print("Please answer 'yes' or 'no'.")
    
    print('\nBaby bag:', baby_bag)
    print('Items remaining:', items_remaining)
    print ('\nRooms:',rooms_list)
    current_room = input('\nWhich room would you like to go to next? ').capitalize()