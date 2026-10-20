"""INHERITANCE"""

class Factorymumbai:                                            #Parent/super class
    a ="I am an attribute mentioned inside Factory"
    def hello(self):
        print("hello I am a method mentioned inside Factory")

class Factorypune(Factorymumbai):                               # Child/sub class
    pass

obj = Factorymumbai()

obj2 = Factorypune()

print(obj2.hello())