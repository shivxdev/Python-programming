"""OOPS """

#types of attribute 1.CLASS 2.INSTANCE

#1.
class Animal:
    name = "Lion" #Class attribute

    def __init__(self,age):
        self.age = age #instance attribute

    def show(self):                       #instance method
        print(f"Your age is {age}")


    @classmethod
    def hello(cls):                       #Class method
        print("How are you brother")


