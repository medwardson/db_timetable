import sqlite3


def get_student_info(student_num):
    datafound = False
    conn =  sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id={}".format(student_num))
    data = c.fetchone()
    try:
        datafound = True
        return data
    except:
        print("Data not found")
    if datafound == False:
        return datafound
