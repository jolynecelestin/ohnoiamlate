current_room = input('Where are you? ').lower()
baby_bag = []

while True:
    search = input('Would you like to search the room? ').lower()

    if search == 'yes':
        print('You are searching and found…')

        if current_room == 'master bedroom':
            print('…nothing.')

        elif current_room == 'hallway 2':
            print('…nothing.')

        elif current_room == 'nursery':
            print('…a baby!')
            baby_bag.append('baby')

        elif current_room == 'hallway 1':
            print('…nothing.')

        elif current_room == 'bathroom':
            print('…diapers!')
            baby_bag.append('diapers')

        elif current_room == 'bedroom':
            print('…nothing.')

        elif current_room == 'living room':
            print('…a pacifier!')
            baby_bag.append('pacifier')

        elif current_room == 'dining room':
            print('…nothing.')

        elif current_room == 'kitchen':
            print('…a bottle!')
            baby_bag.append('bottle')

        elif current_room == 'laundry room':
            print('…clothes!')
            baby_bag.append('clothes')

        elif current_room == 'entryway':
            print('…a car seat!')
            baby_bag.append('car seat')

        elif current_room == 'outside':
            if len(baby_bag) == 6:
                print('Yay! You got everything, all done!')
                break
            else:
                print('You need to keep looking!')
                current_room = 'entryway'
                continue

        else:
            print('Please enter a proper room name.')

    elif search == 'no':
        print('Okay, moving on.')

    else:
        print("Please answer 'yes' or 'no'.")

    # after searching, let the player move to a new room
    print('\nYour baby bag contains:', baby_bag)
    current_room = input('\nWhich room would you like to go to next? ').lower()