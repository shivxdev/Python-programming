""" QUESTION PRACTICE"""

# QUESTION 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if(num1>num2):
    print("Greatest number is: ", num1)
else:
    print("Greatest number is: ", num2)

# QUESTION 2

gen = str(input("Enter your gender: "))

if gen=="male":
    print("Good morning sir")
elif gen=="female":
    print("Good morning maam")
else:
    print("Enter valid gender")

# QUESTION 3

num = int(input("Enter a number: "))

if num%2==0:
    print("The number is even")
else:
    print("The number is odd")

# QUESTION 4

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if age>=18:
    print("hello ", name, " you are valid voter")
else:
    print("hello ", name, " you are not valid voter")

# QUESTION 5

year = int(input("Enter the year: "))   

if year%100==0 and year%400==0:
    print("The year is a leap year")
elif year%100!=0 and year%4==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")


# QUESTION 6 ..........IF ELIF LADDER QUESTION 

temp = int(input("Enter the temprature in Celsius :"))

if temp<0:
    print("Freezing cold")
elif temp>0 and temp<10:
    print("Very cold")
elif temp>=10 and temp<20:
    print("Cold")
elif temp>=20 and temp<30:
    print("Pleasant")
elif temp>=30 and temp<40:
    print("Hot")
else:
    print("Very Hot")
