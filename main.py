"""
CP1404 2023 Assignment 1
Name: Marys Vineeta Paul
Date started:29/6/2023
GitHub URL:
"""




import csv
import random

FILENAME = 'places.csv'


def loadFile():
    with open(FILENAME) as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


def saveFile(places):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow(place)


def countUnvisited(places):
    return sum(place[3] == "n" for place in places)


def listPlaces(places):
    for i, place in enumerate(places):
        print(f"*{i + 1}. {place[0]:<8} in {place[1]:<12} {place[2]:<2}")
    notVisited = countUnvisited(places)
    if notVisited == 0:
        print(f"{len(places)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(places)} places. You still want to visit {notVisited} places.")


def recommendPlace(places):
    notVisited = [place for place in places if place[3] == "n"]
    if len(notVisited) == 0:
        print("No places left to visit!")
    else:
        place = random.choice(notVisited)
        print(f"Not sure where to visit next?")
        print(f"How about... {place[0]} in {place[1]}?")


def addPlace(places):
    name, country, priority = '', '', ''
    while not name or not country or not priority.isdigit():
        if not name:
            name = input("Name: ")
            if not name:
                print("Input cannot be blank")
        elif not country:
            country = input("Country: ")
            if not country:
                print("Input cannot be blank")
        else:
            priority = input("Priority: ")
            if not priority:
                print("Input cannot be blank")
            elif not priority.isdigit():
                print("Invalid input; enter a valid number")
            else:
                priority = int(priority)
                places.append((name, country, priority, "n"))
                print(f"{name} in {country} (priority {priority}) added to Travel Tracker")
                break


def markPlace(places):
    unvisitedCount = countUnvisited(places)
    if unvisitedCount == 0:
        print("No unvisited places")
        return

    listPlaces(places)
    while True:
        choice = input("Enter the number of a place to mark as visited: ")
        if not choice.isdigit():
            print("Invalid input; enter a valid number")
            continue
        pos = int(choice)
        if pos < 1:
            print("Number must be > 0")
            continue
        if pos > len(places):
            print("Invalid place number")
            continue
        break

    name, city, country, status = places[pos - 1]
    if status == "v":
        print(f"You have already visited {name}")
    else:
        places[pos - 1][3] = "v"
        print(f"Congratulations! You have marked {name} in {city}, {country} as visited.")


def showMenu():
    print("Menu:")
    print("L - List places")
    print("R - Recommend random place")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def main():
    print("Travel Tracker 1.0 - by Marys Vineeta Paul")

    places = loadFile()
    print(f"{len(places)} places loaded from places.csv")
    while True:
        showMenu()
        menuChoice = input(">>> ")
        

        if menuChoice.upper() == "L" or menuChoice.lower() == "l":
            listPlaces(places)
        elif menuChoice.upper() == "R" or menuChoice.lower() == "r":
            recommendPlace(places)
        elif menuChoice.upper() == "A" or menuChoice.lower() == "a":
            addPlace(places)
        elif menuChoice.upper() == "M" or menuChoice.lower() == "m":
            markPlace(places)
        elif menuChoice.upper() == "Q" or menuChoice.lower() == "q":
            break
        else:
            print("Invalid menu choice")


    saveFile(places)
    print(f"{len(places)} places saved to {FILENAME}")
    print("Have a nice day :)")


main()
