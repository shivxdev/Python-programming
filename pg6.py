#create and write a text
try:
    with open("welcome.txt","w") as file:
        file.write("welcome to python programming.\n")
        file.write("I am learning file handling.\n")
        file.write("This is our first practical excercise.\n")
    print("File created and data written sucessfully.")
except PermissionError:
    print("Error:You do not have permission to write this file")
except OSError as e:
    print("File operation failed")
