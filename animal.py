class Animal:
    def __init__(self,name):
        self.name = name
        
        def speak(self):
            pass


class dog(Animal):
    def speak(self):
        print("woof")


class cat(Animal):
    def speak(self):
        print("meow")

d = dog("Buddy")
c = cat("kitty")

d.speak()
c.speak()