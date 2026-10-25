"""Enapsulation -: Private attributee and methods"""

class Factory:
    __a = "Pune"

    def __show(self):
        print("Hello i am a factory pune")
                                              #To make it private use 2 underscores
class Bhopal(Factory):
    def show2(self):
        print(super().__a)

obj = Bhopal()
obj.show2()