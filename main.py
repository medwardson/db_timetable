import sqlite3
import add_student
import find_student
import delete_student
import edit_student

while __name__ == "__main__":
    print("Welcome to the TimeTable Program.\n Please select from our following options:")
    choice = input(""">> Add new student (1)
                    \n>> Get a student's Info (2)
                    \n>> Delete a student (3)
                    \n>> Edit student's classes (4)
                    \n>> Quit (5)
                    \n>> """)

    if int(choice) == 1:
        add_student.add_student()
    elif int(choice) == 2:
        student_num = input("Please enter the student's number >> ")
        data = find_student.get_student_info(int(student_num))
        print(data)
    elif int(choice) == 3:
        student_num = input("Please enter the student's number >> ")
        delete_student.del_student(int(student_num))
    elif int(choice) == 4:
        student_num = input("Please enter the student's number >> ")
        edit_student.edit_schedule(int(student_num))
    else:
        print("Thanks for using the program.")
        quit()
