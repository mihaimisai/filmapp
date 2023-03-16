from connect import *

def insert():
    record = []
    title = input("Enter movie title: " )
    year = int(input("Enter year of the movie: "))
    rating = input("Enter the rating: ")
    duration = int(input("Enter duration of movie: "))
    genre = input("Enter the genre of the movie: ")

    record.append(title)
    record.append(year)
    record.append(rating)
    record.append(duration)
    record.append(genre)

    cursor.execute("INSERT INTO tblFilms VALUES (NULL, ?, ?, ?, ?, ?)", record)
    conn.commit()

    print(f"{title} added as follows: {record}")

if __name__ == "__main__":
    insert() # call/invoke the function/subroutine