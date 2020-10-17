"""
open database and check number
if the number exist return false else return true

"""
import sqlite3

def Check_Student(student_num):
    conn =  sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id={}".format(student_num))
    data = c.fetchone()
    if data == None:
        return True
    else:
        return False
