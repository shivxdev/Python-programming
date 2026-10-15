"""WHILE LOOPS"""
# while condn :
   
   #statements

a = 1
while a<=30:
    print(a)
    a = a+1


x = int(input("Enter a number"))

while x>0:
    print (x%10)
    x = x//10


#TO PRINT NUMBER IN REVERSE

r = int(input("Enter the number"))
rev = 0

while r>0:
    rev = rev*10+ r%10
    r = r//10

print(rev)

#PALINDROMIC 

r = int(input("Enter the number"))
copy=r
rev = 0

while r>0:
    rev = rev*10+ r%10
    r = r//10

print(rev)

if copy==rev:
        print("It is a palindrome ")
else:
        print("Not a palindrome")