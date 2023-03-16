from connect import *

def update():
    filmID = int(input("Enter the filmID: "))
    key = int(input("Choose a field name to update. Enter:\n1. Title\n2. Year released\n3. Rating\n4. Duration\n5. Genre\n"))
    fieldName = ""
    if key == 1:
        fieldName = "title"
    if key == 2:
        fieldName = "yearReleased"
    if key == 3:
        fieldName = "rating"
    if key == 4:
        fieldName = "duration"
    if key == 5:
        fieldName = "genre"

    value = input("Type the new value for your chosen field name: ")
    value = "'" + value + "'"
    
    cursor.execute(f"UPDATE tblFilms SET {fieldName} = {value} WHERE filmID = {filmID}")
    conn.commit()

    print(f"The {fieldName} of the movie with id:{filmID} has been updated to {value}")

if __name__ == "__main__":
    update() # call/invoke the function/subroutine