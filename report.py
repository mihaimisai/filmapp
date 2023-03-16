from connect import *

def allFilms():
    cursor.execute("SELECT * FROM tblFilms;")
    row = cursor.fetchall()
    for x in row:
        print(x)


def title():
    title = input("Enter title: ")

    option = 0 
    while option not in [1, 2, 3, 4]:
        print("Title Options\nEnter to search for:\n1. Title Match.\n2. Title begins with.\n3. Title ends with.\n4. Title contains.")

        option = int(input("Enter an option from the Menu choices above: "))
        if option not in [1, 2, 3, 4]:
            print(f"{option} not a valid choice!")
    
    if option == 1:
        cursor.execute(f"SELECT * FROM tblFilms WHERE title = '{title}'")
    elif option == 2:
        cursor.execute(f"SELECT * FROM tblFilms WHERE title LIKE '{title}%'")
    elif option == 3:
        cursor.execute(f"SELECT * FROM tblFilms WHERE title LIKE '%{title}'")
    elif option == 4:
        cursor.execute(f"SELECT * FROM tblFilms WHERE title LIKE '%{title}%'")
    else:
        print("\nInvalid choice\n")

    row = cursor.fetchall()
    for x in row:
        print(x)
    #option to search exactly, to search that it begins, contains or end

def year():
    year = int(input("Enter year of release: "))

    option = 0
    while option not in [1, 2, 3]:
        print("Year Options\nEnter to search the year:\n1. Exactly.\n2. Before.\n3. After.")

        option = int(input("Enter an option from the Menu choices above: "))
        if option not in [1, 2, 3]:
            print(f"{option} not a valid choice!")
    print(option)
    if option == 1:
        cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {year}")
    elif option == 2:
        cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased <= {year}")
    elif option == 3:
        cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased >= {year}")
    else:
        print("Invalid choice")
    
    row = cursor.fetchall()
    for x in row:
        print(x)
    #option to search exactly, before or after

def rating():
    rating = input("Enter rating: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = {rating};")
    row = cursor.fetchall()
    for x in row:
        print(x)

def duration():
    duration = input("Enter duration: ")

    option = 0
    while option not in [1, 2, 3]:
        print("Year Options\nEnter to search the year:\n1. Exactly.\n2. More than.\n3. Less than.")

        option = int(input("Enter an option from the Menu choices above: "))
        if option not in [1, 2, 3]:
            print(f"{option} not a valid choice!")
    print(option)
    if option == 1:
        cursor.execute(f"SELECT * FROM tblFILMS WHERE duration = {duration}")
    elif option == 2:
        cursor.execute(f"SELECT * FROM tblFILMS WHERE duration >= {duration}")
    elif option == 3:
        cursor.execute(f"SELECT * FROM tblFILMS WHERE duration <= {duration}")
    else:
        print("Invalid choice")

    row = cursor.fetchall()
    for x in row:
        print(x)
    #option to search exactly, more or less
    
def genre():
    genre = input("Enter genre: ")
    cursor.execute(f"SELECT * FROM tblFILMS WHERE genre = {genre}")
    row = cursor.fetchall()
    for x in row:
        print(x)

if __name__ == "__main__":
    allFilms()
    title()
    year()
    rating()
    genre()
