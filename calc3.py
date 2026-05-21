def calculater():
    try:
        num1 = float(input("enter the first number:"))
        op = input("choose the operation(+,-,*,/):")
        num2 = float(input("enter the second number:"))
        if op == '+':
            print(num1 + num2)
        elif op == '-':
            print(num1 + num2)
        elif op == '*':
            print(num1 * num2)
        elif op == '/':
            if num2 == 0:
                print("Cannot divide by 0")
            else:
                print(num1 / num2)
        else:
            print("invalid operation")
    except ValueError:
        print("invalid value")
calculater()

