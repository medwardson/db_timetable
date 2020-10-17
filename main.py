import sqlite3
import add_student

while __name__ == "__main__":
    print("Welcome to the TimeTable Program.\n Please select from our following options:")
    choice = input(">> Add new student (1)\n>> Quit (2)\n>> ")
    if int(choice) == 1:
        add_student.add_student()
    else:
        print("Thanks for using the program.")
        quit()
    
