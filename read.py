from connect import *

def read():
    cursor.execute("SELECT * FROM tblFilms") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for x in row:
        print(x)

if __name__ == "__main__":
    read() # call/invoke the function/subroutine