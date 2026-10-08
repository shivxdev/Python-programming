#count vowels,consonent,digits and space
with open("data.txt", "r") as file:
    data = file.read()

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in data:
    if ch.lower() in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch.isspace():
        spaces += 1

print("Vowels     :", vowels)
print("Consonants :", consonants)
print("Digits     :", digits)
print("Spaces     :", spaces)
