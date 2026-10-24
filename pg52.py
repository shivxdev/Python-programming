"""POLYMORPHISM -> OVERWRITING METHOD """


class Animal:
    def show(self):
        print("Hello,I am shivam ")

    # def show(self,name):   This is method overloading 

class Human(Animal):
    def show(self):
        print("How aare you shivam")

obj = Human()
obj.show()    #ye function child class ko call kr rha hai na ki parent class ko ...jbb ki dono jgh same function hai ....isko hi over writing bolte hai 