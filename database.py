import sqlite3

conn =  sqlite3.connect('students.db')

c = conn.cursor()

c.execute("""CREATE TABLE students (
    first text,
    last text,
    id integer,
    p1 text,
    p2 text,
    p3 text,
    p4 text)""")

# c.execute("INSERT INTO students VALUES ('Mark', 'Edwardson', '2556421', 'Calculus', 'English', 'Physics', 'Chemistry')")

# c.execute("SELECT * FROM students WHERE last='Edwardson'")
# print(c.fetchmany(4))

conn.commit()

conn.close()

