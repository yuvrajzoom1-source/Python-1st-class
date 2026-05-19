import random
playing = True 
number= str(random.randint(0,9))

print("I will generate a number from 0 to 9, and you have yo guess the number one at a time")

print("the game ends when you get 1 hero!")

while playing:
    guess = input("give me your best guess! \n")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break

else:
    print("Your guess isn't quite right, try again. \n")

      