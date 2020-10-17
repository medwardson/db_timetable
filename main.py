import sqlite3
import add_student
import find_student

while __name__ == "__main__":
    print("Welcome to the TimeTable Program.\n Please select from our following options:")
    choice = input(">> Add new student (1)\n>> Get a student's Info (2)\n>> Quit (3)\n>> ")
    if int(choice) == 1:
        add_student.add_student()
    elif int(choice) == 2:
        student_num = input("Please enter the student's number >> ")
        find_student.get_student_info(int(student_num))
    else:
        print("Thanks for using the program.")
        quit()
