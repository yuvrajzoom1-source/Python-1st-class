try:
    age = int(input("Enter your age: "))

    # Raise error if age is invalid
    if age < 0 or age > 120:
        raise ValueError("Invalid age entered!")

    print("Age entered is correct.")

    # Checking even or odd
    if age % 2 == 0:
        print("The age is Even.")
    else:
        print("The age is Odd.")

except ValueError as ab:
    print("Error:", ab)