#1

a = int(input("Enter a number : "))

for i in range(a):
    print("Hello World")

#2
m = int(input("Enter a number : "))
for i in range(1, m + 1):
    print(i)

#3
x = int(input("Enter a number :"))
for i in range(x,0,-1):
    print(i)

#4
n = int(input("Which table you want to print :"))
for i in range(n,n*11,n):  
    print(i)

#5

p = int(input("Enter a number : "))
sum = 0
for i in range(1,p+1):
    sum = sum + i
    print(f"The sum is : {sum}")