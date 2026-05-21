def calculater():
    try:
        num1 = float(input("Enter the first number:"))
        op = input("Choose the operator(+,-,*,/):")
        num2 = float(input("Enter the second number:"))
        if op == '+':
            print(num1 + num2)
        elif op == '-':
            print(num1 - num2)
        elif op == '*':
            print(num1 * num2)
        elif op == '/':
            if num2 == 0:
                print("Cannot divide by 0")
            else:
                print(num1 / num2)
        else:
            print("Invalid operation")
    except ValueError:
        print("invalid value")
calculater()