import sqlite3
import find_student
import Check_Student_ID

def add_student():
    first = input("Enter the first name >> ")
    last = input("Enter the last name >> ")
    studentid = int(input("Enter student ID >> "))
    while True:
        if Check_Student_ID.Check_Student(studentid) == False:
            studentid = int(input("Student Id already in use... enter new one \nEnter student ID >> "))
        else:
            break


    p1 = input("Enter period 1 course >> ")
    p2 = input("Enter period 2 course >> ")
    p3 = input("Enter period 3 course >> ")
    p4 = input("Enter period 4 course >> ")

    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(first, last, studentid, p1, p2, p3 ,p4))
    conn.commit()
    conn.close()
