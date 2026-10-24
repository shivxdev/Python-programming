"""POLYMORPHISM -> DUCTILE METHOD"""

class Animal:
    def show(self):
        print("I am showing python code")

class Human:
    def show(self):
        print("I am also showing same ")

obj = Animal()
obj2 = Human()

obj.show()
obj2.show()