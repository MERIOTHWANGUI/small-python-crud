import json

FILE_NAME = "students.json"


# ---------- LOAD & SAVE ----------
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ---------- CREATE ----------
def add_student(students):
    sid = int(input("Enter student ID: "))

    for s in students:
        if s["sid"] == sid:
            print("Student already exists ❌")
            return

    sname = input("Enter student name: ")
    scourse = input("Enter course: ")

    student = {
        "sid": sid,
        "sname": sname,
        "scourse": scourse
    }

    students.append(student)
    save_students(students)
    print("Student added successfully ✅")


# ---------- READ ----------
def view_students(students):
    if not students:
        print("No students found.")
        return

    for s in students:
        print(f"ID: {s['sid']} | Name: {s['sname']} | Course: {s['scourse']}")


# ---------- UPDATE ----------
def update_student(students):
    sid = int(input("Enter student ID to update: "))

    for s in students:
        if s["sid"] == sid:
            s["sname"] = input("Enter new name: ")
            s["scourse"] = input("Enter new course: ")
            save_students(students)
            print("Student updated successfully ✏️")
            return

    print("Student not found ❌")


# ---------- DELETE ----------
def delete_student(students):
    sid = int(input("Enter student ID to delete: "))

    for s in students:
        if s["sid"] == sid:
            students.remove(s)
            save_students(students)
            print("Student deleted successfully 🗑️")
            return

    print("Student not found ❌")


# ---------- MAIN MENU ----------
students = load_students()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        update_student(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice ❌")
