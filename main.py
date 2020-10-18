import sqlite3
import add_student
import find_student
import delete_student
import edit_student
import datetime
import time

while __name__ == "__main__":
    print("\nWelcome to the TimeTable Program. Please select from our following options:")
    choice = input("""\n>> Add new student (1)
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
        dt = datetime.datetime.today()
        try:
            print("\n**********************************************")
            print("Here is {} {}'s schedule for {}/{}/{}:".format(data[0], data[1], dt.year, dt.month, dt.day))
            print(">>> Period 1: {}".format(data[3]))
            print(">>> Period 2: {}".format(data[4]))
            print(">>> Period 3: {}".format(data[5]))
            print(">>> Period 4: {}".format(data[6]))
            print("**********************************************\n")
            time.sleep(5)
            print("Redirecting back to main menu now...")
            time.sleep(2)
        except:
            print("No student found with this number.")
            print("**********************************************\n")
    elif int(choice) == 3:
        student_num = input("Please enter the student's number >> ")
        delete_student.del_student(int(student_num))
        time.sleep(1)
    elif int(choice) == 4:
        student_num = input("Please enter the student's number >> ") 
        try:
            edit_student.edit_schedule(int(student_num))
        except:
            print("No student found with this number.")
    else:
        print("Thanks for using the program.")
        quit()
