start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Creating list of square values
square_list = []

for i in range(start, end + 1):
    square = i ** 2
    square_list.append(square)


even_squares = []
odd_squares = []

for num in square_list:
    if num % 2 == 0:
        even_squares.append(num)
    else:
        odd_squares.append(num)


print("Square Values:", square_list)
print("Even Square Values:", even_squares)
print("Odd Square Values:", odd_squares)