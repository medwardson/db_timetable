import sqlite3
import find_student
import Check_Student_ID

def add_student():

    first = input("Enter the student's first name >> ")
    last = input("Enter the student's last name >> ")
    studentid = int(input("\nEnter student ID >> "))
    while True:
        if Check_Student_ID.Check_Student(studentid) == False:
            studentid = int(input("Student Id already in use... enter new one \nEnter student ID >> "))
        else:
            break
    while True:
        Term = int(input("\ninput the number for the school term you want to input your classes for: \n1. Fall \n2. Winter \n -->> "))
        if Term == 1:
             Fall_p1 = input("\nEnter Fall Term class 1 course code >> ")
             Fall_p2 = input("\nEnter Fall Term class 2 course code >> ")
             Fall_p3 = input("\nEnter Fall Term class 3 course code >> ")
             Fall_p4 = input("\nEnter Fall Term class 4 course code >> ")
             break
        elif Term == 2:
             Winter_p1 = input("\nEnter Winter Term class 1 course code >> ")
             Winter_p2 = input("\nEnter Winter Term class 2 course code >> ")
             Winter_p3 = input("\nEnter Winter Term class 3 course code >> ")
             Winter_p4 = input("\nEnter Winter Term class 4 course code >> ")
             break
        else:
            print("\nInvalid input, TRY AGAIN")
            continue



    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(first, last, studentid, p1, p2, p3 ,p4))
    conn.commit()
    conn.close()
