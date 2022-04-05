#Farnoosh Razavi

rooms = {
    'Hogwarts Library': ['No items in this room', {'South': 'Gryffindor dorm'}],
    'Gryffindor dorm': ['Tom Riddle’s diary', {'North': 'Hogwarts Library', 'West': 'Gaunt Family Shack'}],
    'Gaunt Family Shack': ['Marvolo Gaunt’s ring', {'East': 'Gryffindor dorm', 'South': 'Grimmauld Place'}],
    'Grimmauld Place': ['Salazar Slytherin’s locket', {'West': 'Bellatrix Lestrange’s Gringotts vault', 'North': 'Gaunt Family Shack', 'South': 'The Room of Requirement', 'East': 'Hogwarts Great Hall'}],
    'Bellatrix Lestrange’s Gringotts vault': ['Helga Hufflepuff’s cup', {'East': 'Grimmauld Place'}],
    'The Room of Requirement': ['Rowena Ravenclaw’s diadem', {'North': 'Grimmauld Place', 'East': 'The Forbidden Forrest'}],
    'Hogwarts Great Hall': ['Nagini the snake', {'North': 'Hogwarts Backyard', 'West': 'Grimmauld Place'}],
    'The Forbidden Forrest': ['a part of Voldemort’s soul left in Harry Potter', {'West': 'The Room of Requirement'}],
    'Hogwarts Backyard': ['Lord Voldemort', {'South': 'Hogwarts Great Hall'}]
}



state = 'Hogwarts Library'
inventory = []

# function
def show_instructions():
    print('Harry Potter Text Game')
    print('Collect all of the 7 items to defeat Lord Voldemort!')
    print('Move Commands: South, North, East, and West')
    print("Add to inventory: 'Item Name'")
    print()


# function
def get_new_state(state, direction):
    new_state = state  # declaraing
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state = rooms[i][direction]  # assigning new_state
    return new_state  # return


# function
def get_item(state):
    return rooms[state][0]  # returning Item value


print()
show_instructions()
inventory = []

while 1:
    print("You are in", state)
    print('You currently have', inventory)  # printing inventory
    item = get_item(state)  # calling get_item function
    if item != 'None':
        print('In this room the item is', item)
    if item == 'Lord Voldemort':
        print('\nBattling with Lord Voldemort', end='')
        print()
        if len(inventory) == 7:
            print('You won - Congratulations')
        else:
            print('Sorry, you lost - collect all seven items next time!')
        print()
        exit(0)

    print()
    direction = input('Enter your move: ')  # asking user
    if (direction.lower() == 'east' or direction.lower() == 'west' or
            direction.lower() == 'north' or direction.lower() == 'south'):  # if
        direction = direction[:].capitalize()
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            print('The room has wall in that direction enter other direction!')  # print
        else:
            state = new_state  # changing state value to new_state
    elif direction.lower() == str('get '+item.lower()):  # if
        if item.capitalize() in inventory:  # if item already present in inventory
            print('Item already taken go to another room!!')
        else:
            inventory.append(item.capitalize())  # appending
    else:
        print('Invalid direction!!')  # print