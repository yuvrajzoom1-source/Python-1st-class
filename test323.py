# Four students as tuples
student1 = ("Alice", 1)
student2 = ("Bob", 2)
student3 = ("Charlie", 3)
student4 = ("David", 4)

# Dictionary for grades
grades = {
    1: [85, 90, 78],
    2: [70, 88, 92],
    3: [95, 80, 85],
    4: [60, 75, 70]
}

# Set of subjects
subjects = {"Math", "Science", "English"}

# List of all students
students_list = [student1, student2, student3, student4]

# Display
print("Subjects:", subjects)
print("\nStudents List:", students_list)
print()

for student in students_list:
    print("Student:", student[0])
    print("Roll No:", student[1])
    print("Marks:", grades[student[1]])
    print()
