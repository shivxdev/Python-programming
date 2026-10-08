#Student record file handling
with open("students.txt", "w") as file:
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        marks = float(input("Enter marks: "))

        file.write(f"{roll},{name},{marks}\n")


print("\nStudent Records:")

with open("students.txt", "r") as file:
    for line in file:
        roll, name, marks = line.strip().split(",")

        print("Roll No :", roll)
        print("Name    :", name)
        print("Marks   :", marks)
        print("-------------------")
