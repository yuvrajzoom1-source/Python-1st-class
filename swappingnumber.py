a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

print("Before swapping")
print("a =",a,"b =", b,"c =", c)

temp = a
a = b
b = c
c = temp

print("after spawpping")
print("a =", a,"b =",b,"c =", c)