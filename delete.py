from connect import *
from time import sleep
from read import *


def delete():
    # which field can be use to delete a song in a table(songs)?
    filmID = int(input("Enter the filmID of the record to be deleted: "))

    cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {filmID}")
    # cursor.execute(f"DELETE FROM songs WHERE SongID = >50")
    
    conn.commit()

    print(f"Deleted: {filmID}")

if __name__ == "__main__":
    delete()