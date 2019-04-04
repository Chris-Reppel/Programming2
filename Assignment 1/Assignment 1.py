"""
Chris Reppel
Due: 5/4/19
Travel Tracker 1.0
URL: https://github.com/CP1404-2019-1/assignment1-Mystyking
URL to my original repository where i committed it:
https://github.com/Mystyking/Programming2/tree/master/Assignment%201
"""

import csv

MENU = """Menu:
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit"""


"""This is the main function. It displays a menu and asks the user for their input. If the input is the 
letter L, it will display a list of places from a loaded csv file and and then the user will be prompted again.
The user can then choose to mark the place as visited, add a new place or quit the program."""


def main():
    print("Travel Tracker 1.0 - by Chris Reppel")
    places_list = load_places()  # Load the csv file
    print(MENU)  # Display menu
    choice = input(">>> ").upper()  # User input
    while choice != "Q":
        if choice == "L":
            list_places(places_list)  # Run list function
        elif choice == "A":
            add_new_place(places_list)  # Run Add new place function
        elif choice == "M":
            list_places(places_list)  # Run the list function again but ask the user which place they want
            print("Enter the number of a place to mark as visited")
            check_unvisited(places_list)  # When user chooses place the place is checked if they have already visited it
        else:
            print("Invalid menu choice")  # All other inputs are invalid
        print(MENU)
        choice = input(">>> ").upper()
    save_places(places_list)  # If the user quits the csv file is saved
    print("Have a nice day :)")


"""This function loads the list of places from the csv by splitting all of the words and removing all of the commas"""


def load_places():
    places_list = []
    for place in open('places.csv', 'r'):  # Open csv file for reading
        place = place.rstrip('\n').split(",")
        places_list.append(place)
    for place in places_list:
        place[2] = int(place[2])  # Change the priority to integers
    print('{} places loaded from places.csv'.format(len(places_list)))  # Print how many places the file has
    return places_list


"""This function runs when the user selects L from the menu and it lists the places from the csv. This is where the
output table is formatted to the longest words and lines everything up neatly"""


def list_places(places_list):  # Displays the list from file
    unvisited_place = 0
    longest_place = 0
    longest_country = 0
    place_index = 1

    for place in places_list:
        if len(place[0]) > longest_place:  # The first column is formatted to the place with the longest name
            longest_place = len(place[0])
        if place[3] == 'n':  # Count the number of unvisited places
            unvisited_place += 1
        if len(place[1]) > longest_country:  # The second column is formatted to the country with the longest name
            longest_country = len(place[1])
    for place in places_list:  # Prints the table as Place, Country, Priority with asterisks showing unvisited places
        print(("*" if (place[3] is 'n') else " "), " {}.".format(place_index),
              place[0], " " * (longest_place - len(place[0])), "in", place[1],
              " " * (longest_country + 1 - len(place[1])), "priority", " " * (3 - len(str(place[2]))), place[2])
        place_index += 1
    print(place_index - 1, " places.")  # Print the number of places in the list
    if unvisited_place == 0:  # When all places are visited, prompt user to add a new one
        print("No places left to visit. Why not add a new place?")
    else:  # Print the number of places the user wants to visit
        print("You still want to visit", unvisited_place, "places.")


""""This function runs when the user selects A from the menu. It asks the user for a new place, country and priority"""


def add_new_place(places_list):
    place = record_input("Name:")
    country = record_input("Country:")
    priority = record_input("Priority:")
    new_place = [place, country, priority, 'n']  # How the new place will be stored and displayed
    places_list.append(new_place)  # Saves new place to the csv file


"""This is from the add new place function and it stores the users input for a new place"""


def record_input(input_type):
    if input_type == "Priority:" or input_type == 'place_index':
        data_type = int  # Store the Priority input as an integer

    else:
        data_type = str  # Everything else store as strings

    if input_type == 'place_index':
        input_type = '>>>'

    user_input = input("{} ".format(input_type))
    while verify_input(user_input, data_type) == 0:
        user_input = input("{} ".format(input_type))
    if data_type == int:
        user_input = int(user_input)
    return user_input


"""This function uses the stored data and checks if the input is valid. If not the add new place function runs again"""


def verify_input(user_input, data_type):
    if data_type == str:
        if not user_input.strip():
            print("Input can not be blank")  # Error message when user doesn't enter anything
            return False
        else:
            return True
    else:
        try:
            user_input = int(user_input)
            if user_input <= 0:
                print("Number must be > 0")  # Error message when user enters a number less than 0
                return False
            else:
                return True
        except ValueError:
            print("Invalid input; enter a valid number")  # Error message when user doesnt enter a number where required
            return False


"""This function checks if the user has any places that are unvisited and tells them"""


def check_unvisited(places_list):
    unvisited = 0
    for place in places_list:
        if place[3] == 'n':
            unvisited += 1
            visited_place(places_list)  # Check if user has any unvisited places. If so run the visited_place function
            break
    if unvisited == 0:
        print("No unvisited places")  # Prints if all places have been visited


"""This function runs when the user selects M. It marks a place as visited"""


def visited_place(places_list):
    user_input = record_input('place_index')
    if user_input > len(places_list):  # Number can't be larger than the list so its an Invalid input
        print('Invalid place number')
        visited_place(places_list)
    elif places_list[user_input - 1][3] == 'v':  # The has already marked the place as visited
        print('That place is already visited')
    else:  # Print the place and country they selected as visited
        print(places_list[user_input - 1][0], " in ", places_list[user_input - 1][1], " visited!")
        places_list[user_input - 1][3] = 'v'  # Change the place in the file to visited


"""This function runs when the user selects Q. It saves the changes the user made and changes back to a csv file"""


def save_places(places_list):
    for place in places_list:
        place[2] = str(place[2])  # Convert the priority back to a string for the csv file
    output_file = open('places.csv', 'w')  # Save over the original file
    for place in places_list:
        print(','.join(place), file=output_file)
    output_file.close()  # Close the file (ALWAYS)
    print(len(places_list), " places saved to places.csv")  # Print the number of places that were saved in the file


main()

