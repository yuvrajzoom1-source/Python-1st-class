num = int(input("enter a number:"))

binary = ""

while num>0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("binary number is:", binary)