#Replace a word in file
with open("data.txt", "r") as file:
    data = file.read()

old_word = input("Enter old word: ")
new_word = input("Enter new word: ")

data = data.replace(old_word, new_word)

with open("data.txt", "w") as file:
    file.write(data)

print("Word replaced successfully")
