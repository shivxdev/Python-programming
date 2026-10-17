"""Exception Handling -: #Exception are unexpected events or errors that occurs during the execution of he program , which disrupt the normal flow of the program
   TRY,EXCEPT,ELSE,FINALLY,RAISE"""

a = int(input("Enter the number : "))
try:
    print(10/a)
except ZeroDivisionError:
    print("Sorry you can't divide by 0")

print("OK i have done the division")


a = int(input("Enter the number : "))
try:
    print(10/a)
except Exception as err:
    print(f"Sorry there is an error as {err}")
else:
    print("Good,there is no exception")
finally:
    print("I will run no matter what ")
age = int(input("Enter your age :"))


"""RAISE"""
if age<10 or age>18:
    raise ValueError("Your age must be bw 10 to 18")
#Raise is used to generate error by myself 
else:
    print("Welcome to the club")

print("Club will start soon")


