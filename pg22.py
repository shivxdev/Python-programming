"""TYPE CONVERSION"""

a = 12

a = str(a)

print(type(a))  #integer to string 

print(a)

b = "12"

b = int(b)

print(type(b))

print(b)

"""BOOL"""

c = 12

print(bool(a))

#There are 7 falsy values in python
""" 0 , 0.0 , '' , (), {}, [],False"""   #Except all are TRUE


#IMPLICIT TYPE CONVERSION  - python automatically converts one data type to another without user involvement. This is called implicit type conversion or coercion.

#for example 

x = 12

print(12/3)  #this will give float value


#when user manually converts the datatypefrom one into another type this will called explicit type conversion or type casting.Using inbuilt function
