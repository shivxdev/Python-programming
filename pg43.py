"""FILE HANDLING PROJECT """
from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}:{items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please tell me your file name :")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p,"w") as fs:
                data = input("What you want to write in this file - ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists")
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read :")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
            print("FILE READED SUCCESSFULLY")
        else:
            print("FILE DOES NOT EXIST")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing your file name ")
            print("Press 2 for overwriting the data of your file ")
            print("Press 3 for appending the content in your file ")

            res = int(input("Tell your choice :"))

            if res == 1:
                name2 = input("Enter your new file name :")
                p2 = Path(name2)
                p.rename(p2)
            if res ==2:
                with open(p,'w') as fs:
                    data = input("Enter what you want to write this will overwrite the data :")
                    fs.write(data)
            if res == 3:
                with open(p,'a') as fs:
                    data = input("Enter what you want to append in the file :")
                    fs.write(" "+data)

    except Exception as err:
        print("An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete :")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("FILE REMOVED SUCCESSFULLY")
        else:
            print("NO SUCH FILE EXIST")
    except Exception as err:
        print("An error occured as {err}")
  


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check = int(input("Please tell what you want to operate :"))

if check ==1:
    createfile()
if check ==2:
    readfile()
if check ==3:
    updatefile()
if check ==4:
    deletefile()