"""CONSTRUCTOR IN INHERITANCE"""

class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Hello your name is {self.name}")


class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)  #Super function in hertitance
        self.age = age

    
    def show(self):                                                           #shoe functionality of super function 
        print(f"Hello your name is {self.name} and your age is {self.age}")


# person1 = Human("Shivam")  #This is instance of your sub/child class
animal1 = Animal("Lion")   #This is instance of your main/parent class
person1 = Human("srishti",18)

person1.show()
animal1.show()
# person1.show()


# multiple inheritance

class glass:
    material1 = "water bottle"

class glass2:
    material2 = "softdrink"

class glass3(glass,glass2):  #child can contain multiple parent
    material3 = "both"

obj = glass3()

print(obj.material1)