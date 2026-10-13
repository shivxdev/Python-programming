"""Loops"""

# range(start,stop,step)

for i in range(0, 101, 5):  #type 1
    print(i)

#============================================

a = range(1,30,2)
for i in a:  #type 2
    print(i)

for i in range(101):     # start as a default 0 and step as a default 1 but hamko stop ko define karna hoga
    print(i)  #type 3

#1

for i in range(16,0,-1):  #type 4
    print(i)

#2

for i in range(50,19,-1):  #type 5
    print(i)

#3

for i in range(-3,-16,-1):  #type 6
    print(i)


n = int(input("Which table you want to print :"))
for i in range(n,n*11,n):  #type 7
    print(i)

a = "SHIVAMKUMAR" 
for i in range(11):
    print(a[i])

b = "SHIVAM IS LEARNING INDUSTRY THINGS"
print(len(b))

for i in range(len(b)):
    print(b[i])

x = "MY NAME IS SHIVAM KUMAR"

for i in x:
    print(i)