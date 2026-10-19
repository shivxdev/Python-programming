"""OOPS """

#types of attribute 1.CLASS 2.INSTANCE

#1.
class Animal:
    name = "Lion" #Class attribute

    def __init__(self,age):
        self.age = age #instance attribute

    def show(self):                       #instance method
        print(f"Your age is {self.age}")


    @classmethod
    def hello(cls):                       #Class method
        print("How are you brother")

    @staticmethod
    def static():
        print("How are you")


obj = Animal(12)

obj.show()
obj.hello()
obj.static()