# 7.python program to serach student record stored

students = {
    101: {"name": "Adhi", "age": 20, "grade": "A"},
    102: {"name": "Pavan", "age": 22, "grade": "B"},
    103: {"name": "Tarak", "age": 21, "grade": "A"},
    104: {"name": "Venu", "age": 23, "grade": "C"},
}
def search_student(student_id):
    if student_id in students:
        print("Student Record Found:")
        for key, value in students[student_id].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Student record not found.")

# Taking user input
search_id = int(input("Enter Student ID to search: "))

# Searching for the student record
search_student(search_id)
