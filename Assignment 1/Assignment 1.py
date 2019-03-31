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


def list_places(places_list):
    unvisited_place = 0
    longest_place = 0
    longest_country = 0
    place_index = 1

    for place in places_list:
        if len(place[0]) > longest_place:
            longest_place = len(place[0])
        if place[3] == 'n':
            unvisited_place += 1
        if len(place[1]) > longest_country:
            longest_country = len(place[1])
    for place in places_list:
        print(("*" if (place[3] is 'n') else " "), " {}.".format(place_index),
              place[0], " " * (longest_place - len(place[0])), place[1],
              " " * (longest_country + 1 - len(place[1])), "priority", " " * (3 - len(str(place[2]))), place[2])
        place_index += 1
    print(place_index - 1, " places.")
    if unvisited_place == 0:
        print("No unvisited places")
    else:
        print("You still want to visit", unvisited_place, "places.")


def add_new_place(places_list):
    place = record_input("Place:")
    country = record_input("Country:")
    priority = record_input("Priority:")
    new_place = [place, country, priority, 'n']
    places_list.append(new_place)


#def record_input():




#def verify_input():




#def check_unvisited():




#def visited_place():




#def save_places():




main()

