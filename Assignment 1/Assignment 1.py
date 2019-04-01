"""
Chris Reppel
Due: 5/4/19
Travel Tracker 1.0
URL: https://github.com/CP1404-2019-1/assignment1-Mystyking
"""

import csv

MENU = """Menu:
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit"""


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
              place[0], " " * (longest_place - len(place[0])), "in", place[1],
              " " * (longest_country + 1 - len(place[1])), "priority", " " * (3 - len(str(place[2]))), place[2])
        place_index += 1
    print(place_index - 1, " places.")
    if unvisited_place == 0:
        print("No places left to visit. Why not add a new place?")
    else:
        print("You still want to visit", unvisited_place, "places.")


def add_new_place(places_list):
    place = record_input("Name:")
    country = record_input("Country:")
    priority = record_input("Priority:")
    new_place = [place, country, priority, 'n']
    places_list.append(new_place)
    print(place, "in", country, "( priority", priority, ")", "added to Travel Tracker")


def record_input(input_type):
    if input_type == "Priority:" or input_type == 'place_index':
        data_type = int

    else:
        data_type = str

    if input_type == 'place_index':
        input_type = '>>>'

    user_input = input("{} ".format(input_type))
    while verify_input(user_input, data_type) == 0:
        user_input = input("{} ".format(input_type))
    if data_type == int:
        user_input = int(user_input)
    return user_input


def verify_input(user_input, data_type):
    if data_type == str:
        if not user_input.strip():
            print("Input can not be blank")
            return False
        else:
            return True
    else:
        try:
            user_input = int(user_input)
            if user_input <= 0:
                print("Number must be > 0")
                return False
            else:
                return True
        except ValueError:
            print("Invalid input; enter a valid number")
            return False


def check_unvisited(places_list):
    unvisited = 0
    for place in places_list:
        if place[3] == 'n':
            unvisited += 1
            visited_place(places_list)
            break
    if unvisited == 0:
        print("No unvisited places")


def visited_place(places_list):
    user_input = record_input('place_index')
    if user_input > len(places_list):
        print('Invalid place number')
        visited_place(places_list)
    elif places_list[user_input - 1][3] == 'v':
        print('That place is already visited')
    else:
        print(places_list[user_input - 1][0], " in ", places_list[user_input - 1][1], " visited!")
        places_list[user_input - 1][3] = 'v'


def save_places(places_list):
    for place in places_list:
        place[2] = str(place[2])
    output_file = open('places.csv', 'w')
    for place in places_list:
        print(','.join(place), file=output_file)
    output_file.close()
    print(len(places_list), " places saved to places.csv")


main()

