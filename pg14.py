#Search a word in File
with open("data.txt", "r") as file:
    data = file.read()

word = input("Enter word to search: ")

words = data.lower().split()
count = words.count(word.lower())

if count > 0:
    print("Word found")
    print("Frequency:", count)
else:
    print("Word not found")
