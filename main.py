import sqlite3
import add_student


if __name__ == "__main__":
    #add_student.add_student()
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE last='Naidoo'")
    print(c.fetchall())
    conn.commit()
    conn.close()
