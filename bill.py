while True:

    bill = int(input("enter bill amount: "))
    paid = int(input("enter paid amount: "))

    due = bill - paid

    print("costomer due is", due)
    ab = input("do u want to continue:")
    if  ab == "no":
        break
    else:
        continue
