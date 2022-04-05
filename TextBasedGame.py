#Farnoosh Razavi
#Harry Potter Text Game


# The dictionary links a room to other rooms.

rooms = {"Hogwarts Library" : {"South" : "Gryffindor dorm"},
        "Gryffindor dorm" : {"North" : "Hogwarts Library", "West" : "Gaunt Family Shack"},
        "Gaunt Family Shack" : {"East" : "Gryffindor dorm", "South" : "Grimmauld Place"},
        "Grimmauld Place" : {"West" : "Bellatrix Lestrange’s Gringotts vault", "North" : 'Gaunt Family Shack', "South" : 'The Room of Requirement', "East" : 'Hogwarts Great Hall'},
        "Bellatrix Lestrange’s Gringotts vault" : {"East" : "Grimmauld Place"},
        "The Room of Requirement" : {"North" : "Grimmauld Place", "East": "The Forbidden Forrest"},
        "Hogwarts Great Hall" : {"North" : "Hogwarts Backyard", "West" : "Grimmauld Place"},
         "Hogwarts Backyard" : {"South" : "Hogwarts Great Hall"},
         "The Forbidden Forrest" : {"West" : "The Room of Requirement"}
}

items = {
    'Hogwarts Library': 'No items in this room',
    'Gryffindor dorm': 'Tom Riddle’s diary',
    'Gaunt Family Shack': 'Marvolo Gaunt’s ring',
    'Grimmauld Place': 'Salazar Slytherin’s locket',
    'Bellatrix Lestrange’s Gringotts vault': 'Helga Hufflepuff’s cup',
    'The Room of Requirement': 'Rowena Ravenclaw’s diadem',
    'The Forbidden Forrest': 'a part of Voldemort’s soul left in Harry Potter',
    'Hogwarts Great Hall': 'Nagini the snake',
    'Hogwarts Backyard': 'Lord Voldemort'

}
state = 'Hogwarts Library'
inventory = []


# function to move between rooms
def get_new_state(state, direction):
    new_state = state  # declaring
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state = rooms[i][direction]  # assigning new_state

    return new_state  # return


while 1:  # gameplay loop to make the announcements and collect the items
    print('You are in the ', state)  # printing state
    if state == 'Hogwarts Backyard':
        print('Battling with Lord Voldemort', end='')
        print()
        if len(inventory) == 7:
            print('You won - congratulations')
        else:
            print('Sorry, you lost - better have all 7 horcruxes next time')
        break

    print('Available to you in this room is: ', items[state])
    print('You currently have', inventory)
    direction = input('Enter item you want OR direction to go: ')  # asking user
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state]) #adding each item in the rooms to the inventory after user gives the order
        continue
    direction = direction.capitalize()  # making first character capital remaining lower
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':  # if
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            print('There are dementors in that direction quickly enter another direction!')  # print
        else:
            state = new_state  # changing state value to new_state
    else:
        print('Invalid direction!!')  # print