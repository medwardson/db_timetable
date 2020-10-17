import sqlite3

def find_student(student_num):
    datafound = False
    conn =  sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id={}".format(student_num))
    data = c.fetchone()
    try:
        datafound = True
        first, last, p1, p2, p3, p4  = data[0], data[1], data[3], data[4], data[5], data[6]
        print(first, last, p1, p2, p3, p4)
    except:
        print("Data not found")
    if datafound == False:
        return



find_student(2556421)