"""ENCAPSULATION"""

#encap means putting data (variable) and code(function) together in one place inside a class

class Factory:
    a = "Pune"

    def show(self):
        print("Hello i am a factory pune")

obj = Factory()

print(obj.a)
obj.show()

class Bhopal(Factory):
    def show2(self):
        print(super().a)

obj2 = Bhopal()
obj2.show2()