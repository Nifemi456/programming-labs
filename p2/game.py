from random import randint

room_items = ["bow", "armour", "boomerang", "shield", "sword"]

def treasure_room():
    print('You have found the ultimate treasure chest! You win the game!')
    return
    
def item_room(items: list):
    global room_items
    item = room_items[randint(0,len(room_items)-1)]
    print (f'You found {item}, you decide to pick it up!')
    items.append(item)
    return
    
def monster_room(items: list):
    print("You have entered a room with a monster!")
    reply = input("Do you choose to fight or flee? ")
    loop = True
    while loop:
        if reply == 'flee':
            print("You fled back to the starting room.")
            loop = False
            return True
        elif reply == 'fight':
            temp = fight_monster(items)
            loop = False
            return temp
        else:
            reply = input("Invalid choice. Please choose to fight or flee? " )
            loop = True
        
def fight_monster(items: list):
    print("You are fighting the monster...")
    temp = randint(0,10)
    
    if temp>(3-len(items)):
        print("You defeated the monster! You win!")
        return True
    else:
        print("The monster defeated you. You lose the game.")
        return False
    
def starting_room():
    visited_rooms = []
    picked_up_items = []
    
    doors = 3
    right_door = randint(1, doors)
    print(f"You are in a room with {doors} doors.")
    temp = True
    while temp:
        choice = int(input(f"Which door (1 - {doors}) do you choose? "))
        visited_rooms.append(choice)
        if choice == right_door:
            treasure_room()
            temp = False
        else:
            coin = randint(0,1)
            if coin == 0:
                item_room(picked_up_items)
            else:
                temp = monster_room(picked_up_items)
    return (visited_rooms, picked_up_items)
                
starting_room()