"""Enapsulation -: Access modifier example"""

class Demo:
    def __init__(self):
        self.name = "Public member"    #Public
        self._age = 20                 #Protected
        self.__salary = 50000          #Private

    def show(self):
        print("Inside the class:")
        print("Public:",self.name)
        print("Protected",self._age)
        print("Private",self.__salary)

