medical_cause = input("do u have a medical cause? Y/N:", ).strip() .upper()
if medical_cause == 'Y':
    print("your allowed")
else:
    atenn = int(input("Enter the attendence of the sutdent"))
if atenn >= 75:
    print("allowed")
else:
    print("not allowed")
