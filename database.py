import sqlite3

conn = sqlite3.connect('students.db')

c = conn.cursor()

# c.execute("""CREATE TABLE students (
#     first text,
#     last text,
#     id integer,
#     p1 text,
#     p2 text,
#     p3 text,
#     p4 text)""")

# c.execute("INSERT INTO students VALUES ('Mesha', 'Naidoo', '2556421', 'Calculus', 'English', 'Physics', 'Chemistry')")
  
# c.execute("SELECT * FROM students WHERE first='Mesha'")
# c.execute("DELETE FROM students WHERE id='2556421'")

c.execute("SELECT * FROM students WHERE id='2556421'")
ossysresult = c.fetchall()
print(ossysresult)

conn.commit()
conn.close()

