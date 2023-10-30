"""Lab 6 Text adventure"""

import random
import arcade

yes = True
no = False

class Room:
    def __init__(self, description=" ", north=0, south=0, east=0, west=0):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():
    room_list = []

    room = Room("You're have entered the South Hall, there is a passage to the North, West and East.",4,None,2,0)
    room_list.append(room)

    room = Room("You have entered the Dining Room, there is a passage to the North and West.",5,None,None,1)
    room_list.append(room)

    room = Room("You have entered Bedroom two, there is a passage to the North and East.", 3, None,1,None)
    room_list.append(room)

    room = Room("You have entered Bedroom 1, there is a passage to the South and East.",None,0,4,None)
    room_list.append(room)

    room = Room("You have entered the North Hall, there is a passage to the North, South, East and West.",6,1,5,3)
    room_list.append(room)

    room = Room("You have entered the Kitchen, there is a passage to the South and West.",None,2,None,4)
    room_list.append(room)

    room = Room("You have entered the Balcony, there is a passage to the South.",None, 4,None,None)
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print()

        current_description = room_list[current_room].description
        print(current_description)

        user_input = input("What would you like to do? ")

        if "north" in user_input.lower():
            print("You headed North.")
            next_room = room_list[current_room].north

            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way. ")

        elif "east" in user_input.lower():
            print("You headed east. ")
            next_room = room_list[current_room].east

            if next_room is not None:
                current_room = next_room
            else:
                print("you can't go that way.")

        elif "south" in user_input.lower():
            print("You headed south. ")
            next_room = room_list[current_room].south

            if next_room is not None:
                current_room = next_room
            else:
                print("you can't go that way.")

        elif "west" in user_input.lower():
            print("You headed west. ")
            next_room = room_list[current_room].west

            if next_room is not None:
                current_room = next_room
            else:
                print("you can't go that way.")

        elif user_input == "quit":
            print("You have Quit the Game, Goodbye :)")
            done = True

        else:
            print("I do not understand. ")


main()

