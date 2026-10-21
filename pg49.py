"""CONSTRUCTOR IN INHERITANCE"""

class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Hello your name is {self.name}")


class Human(Animal):
    pass

person1 = Human("Shivam")  #This is instance of your sub/child class
animal1 = Animal("Lion")   #This is instance of your main/parent class

person1.show()
animal1.show()