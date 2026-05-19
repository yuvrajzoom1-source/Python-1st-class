try:
    inp=int(input("Enter your age:"))
    print("Your age is:",inp)
except ValueError as e:
    print(e)
break