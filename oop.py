class Animal:   
    def __init__(self, name):
        self.name = name 

    def speak(self):      
        pass

class Dog(Animal):        
    def speak(self):  
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")


d = Dog("Buddy")
c = Cat("Kitty")
 

c.speak()   
d.speak() 
