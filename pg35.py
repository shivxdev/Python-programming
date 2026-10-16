#LIST
"""MUTABLE(we can change data after creation of list),ORDERED(indexed),DUPLICATE(allow duplicate value),HETROGENOUS(we can store multiple datatype)"""
fruits = ["apple","banana","cherry"]
numbers = [1,2,3,4,5,6,7,8,9]

a = [10,11,12,13,14,14,14,15]
print(a[0]) #index calling
print(a[0:6]) #Slicing

print(a)

a[0] = 100 #list modification

print(a) #updated list

#using loop -- 1st way using index

for i in range(len(a)):
    print(i)

#using loop -- 2nd way directly on values

for i in a:
    print(i)

#to add something in the last we use "APPEND" method 

a.append(400)
print(a)

#to insert something at any specific place we use "INSERT" method

a.insert(0,99)
print(a)

#to add multiple elements in the last we use "EXTEND"

a.extend([150,250,350])
print(a)

#to remove element from the list we use "REMOVE"

a.remove(99)
print(a)

#"POP" removes and stores the element
a.pop(0)
print(a)

#"COUNT" to count the occurence of number

count_14 = a.count(14)
print(count_14)

#"INDEX" to find the index of the number

index = a.index(150)
print(index)

a.sort()
print(a)

a.reverse()
print(a)

copy = a.copy()
print(copy)

a.clear()
print(a)