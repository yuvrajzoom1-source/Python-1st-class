class IOString():


    def __init__(self):
        self.str1 = ""

    def getstring(self):
        self.str1 = input("enetr string :")

    def pringsrting(self):
        print("result is :", self.str1.upper())


str1 = IOString()

str1.get_String()
str1.print_String()