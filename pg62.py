"""ARGS AND KWARGS"""
#Kwargs - Keyword arguments

def decorate(func):
    def wrapper(*args,**kwargs):
        print("The addition to your numbers are")
        func(*args,**kwargs)
        print("Thankyou I hope you liked it ")
    return wrapper


@decorate
def addition(a,b,c,d):
    print(f"your total is {a+b+c+d}")

addition(10,20,99,78)