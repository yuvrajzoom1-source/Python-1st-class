student1 = ("alice", 1)
student2 = ("bob", 2)
student3 = ("david", 3)

grades = {
    1:[34.54,31],
    2:[56,46,23],
    3:[84,43,98],
}

subjects = {"math","science","english"}

studentlist = [student1, student2, student3]
print("subjects:", subjects)
print("\nStudentlist", studentlist)
print()

for student in studentlist:
    print("student:", student[0])
    print("roll:", student[1])
    print("marks:", grades[student[1]])