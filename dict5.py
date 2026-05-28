student = {
    "name": "Kshitun",
    "class": "V",
    "subject": "Math",
    "teacher": "Kshitun"
}


value = "Kshitun"


count = 0


for v in student.values():
    if v == value:
        count += 1


print("Frequency of", value, "is:", count)