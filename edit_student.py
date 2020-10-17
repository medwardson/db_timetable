import sqlite3
import find_student

def edit_schedule(student_num):
    data = find_student.get_student_info(student_num)
    print(data[0], data[1], "has the following courses:\n", data[3], data[4], data[5], data[6])
    row = input("""Which of the following would you like to update?

                >> First Class (1)
                >> Second Class (2)
                >> Third Class (3)
                >> Fourth Class (4)

                >> """)
    while row != "1" and row != "2" and row != "3" and row != "4":
        row = input("You have not chose a valid option. Please choose a number from 1 to 4.")
    if row == "1":
        row = "p1"
    elif row == "2":
        row = "p2"
    elif row == "3":
        row = "p3"
    elif row == "4":
        row = "p4"
    new_value = input("Enter the new value for {}\n>> ".format(row))
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("UPDATE students SET '{}' = '{}' WHERE id={}".format(row, new_value, student_num))
    conn.commit()
    conn.close