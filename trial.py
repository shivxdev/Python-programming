real = str(input("Enter a string to check if it is a palindrome: "))

reverse = ""

for i in range(len(real)-1,-1,-1):
    reverse = reverse + real[i]

if real == reverse:
    print(f"{real} is a palindrome")
else:
    print(f"{real} is not a palindrome")