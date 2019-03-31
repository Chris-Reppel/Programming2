"""
Chris Reppel
Due: 5/4/19
Travel Tracker 1.0
"""

MENU = """Menu:
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit"""

import csv


def main():
    print("Travel Tracker 1.0 - by Chris Reppel")
    places_list = load_places()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            list_places(places_list)
        elif choice == "A":
            add_new_place(places_list)
        elif choice == "M":
            list_places(places_list)
            print("Enter the number of a place to mark as visited")
            check_unvisited(places_list)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_places(places_list)
    print("Have a nice day :)")


def load_places():
    places_list = []
    for place in open('places.csv', 'r'):
        place = place.rstrip('\n').split(",")
        places_list.append(place)
    for place in places_list:
        place[2] = int(place[2])
    print('{} places loaded from places.csv'.format(len(places_list)))
    return places_list


#def list_places():




#def add_new_place():




#def record_input():




#def verify_input():




#def check_unvisited():




#def visited_place():




#def save_places():




main()

