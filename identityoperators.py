x = 5
if (type(x)is int):
    print(True)
else:
    print(False)

a = 20
b = 20
if (a is b):
    print("a and b are same identity")
b=5
if (a is not b):
    print("a and b are different identity")