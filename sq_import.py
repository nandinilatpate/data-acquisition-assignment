
import pandas as pd
import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()
cursor.execute(""" 
               CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   branch TEXT,
                   marks INTEGER
               )
               """)
cursor.execute("DELETE from students")
students_data = [
    (1,"aksh","computer engineering",85),
    (2,"rahul","ENTC",78),
    (3,"priya","data science",91),
    (4,"sneha","computer engineering",95),
    (5,"amit","mechanical engineering",80),
]
cursor.executemany(
    "INSERT INTO students(id,name,branch,marks) VALUES(?,?,?,?)",
    students_data
)
connection.commit()
query = "SELECT * FROM students"
df = pd.read_sql_query(query,connection)
print("complete dataframe:")
print(df)
connection.close()