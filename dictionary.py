students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88
}
name = input("Enter the student's name: ")
marks = students.get(name.capitalize())

if marks is not None:
    print(f"{name}'s marks : {marks}")
else:
    print(f"Student '{name}' not found .")
