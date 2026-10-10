#Copy on file to Another+statistics
with open("source.txt", "r") as file:
    data = file.read()

with open("destination.txt", "w") as file:
    file.write(data)

lines = data.splitlines()
words = data.split()
characters = len(data)

print("File copied successfully")
print("Lines      :", len(lines))
print("Words      :", len(words))
print("Characters :", characters)
