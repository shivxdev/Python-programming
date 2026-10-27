"""DECORATOR"""

class Animal:
    @property
    def show(self):
        print("Hello ,how are you")

obj = Animal()

obj.show

def decorator(func):
    def wrapper():
        print("I will print myself before the fucntion ")
        func()
        print("I will print after the fucntion")
    return wrapper

@decorator
def hello():
    print("Hello , I am akarsh")

hello()

