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
total = 0
for i in range(1,p+1):
    total = total + i

print(f"The sum is {total}")

#6

num = int(input("Enter the number whose factorial you want:"))
fact = 1

for i in range(num,0,-1):
    fact = fact*i

print(f"The factorial of {num} is {fact}")

#7

ran = int(input("Enter the range :"))
esum = 0
osum = 0
for i in range(1,ran+1):
    if i%2==0:
      esum = esum + i
      print(f"The sum of even numbers in the range is {esum}")
    elif i%2!=0:
      osum = osum + i
      print(f"The sum of odd numbers in the range is {osum}")
    else:
      print("Enter the valid range")


#Type 2

max = int(input("Enter the range :"))
even = 0
odd = 0
for i in range(1,max+1):
   if i%2==0:
      even = even +i
   else:
      odd = odd + i

print(f"The sum of even numbers in the range is {even}")
print(f"The sum of odd numbers in the range is {odd}")

#to take output we have second type of formatted string print 
"""print(f"The sum of even numbers in the range is {even} and the sum of odd numbers in the range is {odd}")
                                          and 
    print(f"The sum of odd and even numbers in the range is {odd} and {even} respectively")"""


#8 print all factors of the number

z = int(input("Enter a number :"))

for i in range(1,z+1):
    if z%i==0:
        print(i)


#9

v = int(input("Enter a number :"))
vsum = 0
for i in range(1,v):
    if v%i==0:
        vsum = vsum + i


if vsum == v:
    print(f"{v} is a perfect number")
else:
    print("Not a perfect number")


#10

p = int(input("Enter a number :"))
count = 0
for i in range(1,p+1):
    if p%i==0:
        count = count + 1

if count == 2:
    print(f"{p} is a prime number")
else:
    print(f"{p} is not a prime number")

#11

