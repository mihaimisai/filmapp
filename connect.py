import sqlite3 as sql

conn = sql.connect("bootcamp/Python/task_project/filmflix.db")

#creating a cursor to navigate the db
cursor = conn.cursor()