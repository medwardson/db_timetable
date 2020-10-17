import sqlite3


def get_student_info(student_num):
    datafound = False
    conn =  sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id={}".format(student_num))
    data = c.fetchone()
    try:
        datafound = True
        first, last, p1, p2, p3, p4  = data[0], data[1], data[3], data[4], data[5], data[6]
        print("************\n",first, last, p1, p2, p3, p4,"\n************\n")
    except:
        print("Data not found")

    
    if datafound == False:
        return datafound
