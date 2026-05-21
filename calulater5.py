def add(a,b):
    return (a+b)
def substract(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def divide(a,b):
    return(a/b)

num1 = float(input("Enter the first number:"))
op = input("choose the opertation(+,-,*,/):")
num2 = float(input("Enter the second number:"))

if op == '+':
    print(add(num1,num2))
elif op == '-':
    print(substract(num1,num2))
elif op == '*':
    print(multiply(num1,num2))
elif op == '/':
    print(divide(num1,num2))
else:
    print("invalid operation")