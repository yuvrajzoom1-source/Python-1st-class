def add(p,q):
    return p + q
def suntract(p,q):
    return p - q
def multiply(p,q):
    return p * q
def divide(p,q):
    return p / q

print ("Please select the operation")
print ("a. add")
print ("b. subtract")
print ("c. multiply")
print ("d. divide")

choice = input("Please enter choice (a/ b/ c/ d):")

num_1 = int(input("please enter the first number:"))
num_2 = int(input("please enter the second number:"))

if choice == 'a':
    print (num_1, " +", num_2 " = ", add(num_1 , num_2))