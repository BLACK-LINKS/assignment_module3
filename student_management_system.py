# Student Management System

students = {} # Dictionary to store student data
logs = [] # List to store transaction logs

def add_student():
    """
    Adds a new student to the student database.
    """
    serial_number = len(students) + 1
    fname = input("Enter First Name: ")
    while True:
        try:
            lname = input("Enter Last Name: ")
            if not lname.isalpha():
                raise ValueError("Last name should only contain alphabets.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            contact = input("Enter Contact Number: ")
            if not contact.isdigit() or len(contact) != 10:
                raise ValueError("Contact number should be a 10-digit number.")
            break
        except ValueError as e:
            print(e)
    subjects = {}
    while True:
        subject = input("Enter Subject (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        while True:
            try:
                marks = int(input("Enter Marks: "))
                if marks < 0 or marks > 100:
                    raise ValueError("Marks should be between 0 and 100.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                fees = int(input("Enter Fees: "))
                if fees < 0:
                    raise ValueError("Fees cannot be negative.")
                break
            except ValueError as e:
                print(e)
        subjects[subject] = {'marks': marks, 'fees': fees}
    faculty = input("Enter Faculty Name: ")
    students[serial_number] = {
        'fname': fname,
        'lname': lname,
        'contact': contact,
        'subject': subjects,
        'faculty': faculty
    }
    logs.append(f"Student {fname} {lname} added with serial number {serial_number}")
    print("Student added successfully!")

def remove_student():
    """
    Removes a student from the student database.
    """
    while True:
        try:
            serial_number = int(input("Enter Serial Number of Student to Remove: "))
            if serial_number not in students:
                raise ValueError("Invalid Serial Number.")
            break
        except ValueError as e:
            print(e)
    confirm = input(f"Are you sure you want to remove student {students[serial_number]['fname']} {students[serial_number]['lname']}? (y/n): ")
    if confirm.lower() == 'y':
        del students[serial_number]
        logs.append(f"Student with serial number {serial_number} removed.")
        print("Student removed successfully!")
    else:
        print("Student removal cancelled.")

def view_all_students():
    """
    Displays all students in the database.
    """
    if not students:
        print("No students in the database.")
        return
    for serial_number, student in students.items():
        print(f"Serial Number: {serial_number}")
        print(f"Name: {student['fname']} {student['lname']}")
        print(f"Contact: {student['contact']}")
        print("Subjects:")
        for subject, details in student['subject'].items():
            print(f"  {subject}: Marks {details['marks']}, Fees {details['fees']}")
        print(f"Faculty: {student['faculty']}\n")

def view_specific_student():
    """
    Displays details of a specific student.
    """
    while True:
        try:
            serial_number = int(input("Enter Serial Number of Student: "))
            if serial_number not in students:
                raise ValueError("Invalid Serial Number.")
            break
        except ValueError as e:
            print(e)
    student = students[serial_number]
    print(f"Name: {student['fname']} {student['lname']}")
    print(f"Contact: {student['contact']}")
    print("Subjects:")
    for subject, details in student['subject'].items():
        print(f"  {subject}: Marks {details['marks']}, Fees {details['fees']}")
    print(f"Faculty: {student['faculty']}")

def add_marks():
    """
    Allows a faculty member to add marks for a student.
    """
    while True:
        try:
            serial_number = int(input("Enter Serial Number of Student: "))
            if serial_number not in students:
                raise ValueError("Invalid Serial Number.")
            break
        except ValueError as e:
            print(e)
    faculty_name = input("Enter Faculty Name: ")
    if faculty_name != students[serial_number]['faculty']:
        print("You are not authorized to access this student's data.")
        return
    while True:
        try:
            subject = input("Enter Subject to add marks: ")
            if subject not in students[serial_number]['subject']:
                raise ValueError("Invalid Subject.")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            marks = int(input("Enter Marks: "))
            if marks < 0 or marks > 100:
                raise ValueError("Marks should be between 0 and 100.")
            break
        except ValueError as e:
            print(e)
    students[serial_number]['subject'][subject]['marks'] = marks
    logs.append(f"Faculty {faculty_name} added marks {marks} for {subject} to student {students[serial_number]['fname']} {students[serial_number]['lname']}.")
    print("Marks added successfully!")

def main():
    """
    Main function for the student management system.
    """
    while True:
        print("Welcome to the Student Management System!")
        print("1. Counsellor")
        print("2. Faculty")
        print("3. Student")
        print("4. Exit")
        role = input("Enter a role id: ")
        if role == '1':
            while True:
                print("Counsellor Menu:")
                print("1. Add Student")
                print("2. Remove Student")
                print("3. View All Students")
                print("4. View Specific Student")
                print("5. Exit to Main Menu")
                choice = input("Enter a choice: ")
                if choice == '1':
                    add_student()
                elif choice == '2':
                    remove_student()
                elif choice == '3':
                    view_all_students()
                elif choice == '4':
                    view_specific_student()
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif role == '2':
            while True:
                print("Faculty Menu:")
                print("1. Add Marks to Student")
                print("2. View All Students")
                print("3. Exit to Main Menu")
                choice = input("Enter a choice: ")
                if choice == '1':
                    add_marks()
                elif choice == '2':
                    view_all_students()
                elif choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif role == '3':
            print("Student functionality is not yet implemented.")
        elif role == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
