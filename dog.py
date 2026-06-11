class Dog:


    animal = "Dog"


    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


    def display(self):
        print("Animal :", Dog.animal)
        print("Breed  :", self.breed)
        print("Name   :", self.name)
        
        print()

dog1 = Dog("Labrador", "Bruno")
dog2 = Dog("German Shepherd", "Rocky")


dog1.display()
dog2.display()