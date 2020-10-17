import sqlite3
import find_student
import Check_Student_ID

def add_student():

    first = input("Enter the student's first name >> ")
    last = input("Enter the student's last name >> ")
    studentid = int(input("Enter student ID >> "))
    while True:
        if Check_Student_ID.Check_Student(studentid) == False:
            studentid = int(input("Student Id already in use... enter new one \nEnter student ID >> "))
        else:
            break


    p1 = input("Enter class 1 course code >> ")
    p2 = input("Enter class 2 course code >> ")
    p3 = input("Enter class 3 course code >> ")
    p4 = input("Enter class 4 course code >> ")

    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES ('{}', '{}', '{}', '\n{}', '\n{}', '\n{}', '\n{}')".format(first, last, studentid, p1, p2, p3 ,p4))
    conn.commit()
    conn.close()
