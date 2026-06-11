import random

print("=== Random Password Generator ===")


length = int(input("Enter password length: "))


characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"


password = ""


for i in range(length):
    random_char = random.choice(characters)
    password = password + random_char


print("Generated Password:", password)