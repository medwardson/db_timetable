import sqlite3
import find_student

def del_student(student_num):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    try:
        data = find_student.get_student_info(student_num)
        print("The following student has been deleted: {} {}".format(data[0], data[1]))
        c.execute("DELETE FROM students WHERE id='{}'".format(student_num))
    except:
        print("Sorry, no student with this ID was found.")
    conn.commit()
    conn.close()
