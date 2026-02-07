def add_student(students):
    sid = int(input("Enter student ID: "))
    sname = input("Enter student name: ")
    scourse = input("Enter course: ")

    for s in students:
        if s["sid"] == sid:
            print("Student already exists.")
            return
    student = {
        "sid": sid,
        "sname": sname,
        "scourse": scourse
    }
    students.append(student)
    print("Student added.")


def view_students(students):
    if not students:
        print("No students available.")
    else:
        for s in students:
            print(s)


def search_student(students):
    query = input("Enter name to search: ").strip().lower()
    found = False

    for s in students:
        if query in s["sname"].lower():
            print("FOUND:", s)
            found = True

    if not found:
        print("Student not found.")


def update_course(students):
    sid = int(input("Enter student ID to update course: "))
    new_course = input("Enter new course: ")

    for s in students:
        if s["sid"] == sid:
            s["scourse"] = new_course
            print("Course updated.")
            return

    print("Student not found.")


def delete_student(students):
    sid = int(input("Enter student ID to delete: "))
    confirm = input("Are you sure? (y/n): ").lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    for s in students:
        if s["sid"] == sid:
            students.remove(s)
            print("Student removed.")
            return

    print("Student not found.")


students = []

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Update course")
    print("4. Delete student")
    print("5. search name")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        update_course(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        search_student(students)
    elif choice == "6":
        break
    else:
        print("Invalid choice")
