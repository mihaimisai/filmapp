from read import *
from insert import *
from update import *
from delete import *
from report import *

def menu():
    option = 0 
    while option not in [1, 2, 3, 4, 5]:
        print("Menu Options\nEnter\n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. Report Menu.\n6. To Exit")

        option = int(input("Enter an option from the Menu choices above: "))
        if option not in [1, 2, 3, 4, 5]:
            print(f"{option} not a valid choice!")
    return option

def report():
    option = 0 
    while option not in [1, 2, 3, 4, 5, 6]:
        print("Report Options\nEnter\n1. To Print All.\n2. Search Title.\n3. Search Year of Release.\n4. Search Ratin.\n5. Search Duration.\n6. Search Genre")

        option = int(input("Enter an option from the Menu choices above: "))
        if option not in [1, 2, 3, 4, 5, 6]:
            print(f"{option} not a valid choice!")
    return option

if __name__ == "__main__":
    mainProgram = True
    while mainProgram:
        mainMenu = menu()
        if mainMenu == 1:
            read()
        elif mainMenu == 2:
            insert()
        elif mainMenu == 3:
            update()
        elif mainMenu == 4:
            delete()
        elif mainMenu == 5:
            reportOption = report()
            if reportOption == 1:
                allFilms()
            elif reportOption == 2:
                title()
            elif reportOption == 3:
                year()
            elif reportOption == 4:
                rating()
            elif reportOption == 5:
                genre()
            else:
                print("Invalid choice")
        