"""FUNCTIONS -: function in python group reuseable code into block that can be executed by calling function name
   EXAMPLE -: print(),input(),len()"""

def greet():
 print(f"Good morning")

greet()

def sum():
 print("The sum of your number is ____")

sum()

#Passing arguments
#type 1 argument (positional argument )
def sum(a,b):
 print(f"The sum of your number is :{a+b}")

sum(12,45)  #yha hame input dena hota hai wrna error ayegaaa 
sum(1234,78)

#type 2 argument(keyword argument)
def hello(name,age):
  print(f"Hello {name} your age is {age}")

hello(age=19,name="Shivam")

#type 3 Default Argument

def difference(a,b=45):
 print(f"The difference is :{a-b}")

difference(100)

#FUNCTION example
def palindrome(st):
    rev =""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st:
        print(f"The {st} is palindromic string")
    else:
        print(f"The {st} is not palindromic")

palindrome("naman")
palindrome("shivam")

#Additional (Use of return)

def hey():
    return"Hey how are you"

print(hey())