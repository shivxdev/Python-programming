import json
from math import inf
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
             data = json.loads(fs.read)
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occured as {err}")

    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "name": input("Enter your name :"),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email:"),
            "pin": int(input("Enter your pin")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age']<18 or len(str(info['pin'])) != 4:
            print("Sorry , You are not Eligible for creating account ")
        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("Please note down your account number ")

            Bank.data.append(info)
            Bank.update()

    def Depositmoney(self):
        accnumber = input("Enter your account number :")
        pin = int(input("Enter your pin aswell :"))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No such account exist")
        else:
            amount = int(input("Enter the amount you want to deposit :"))
            if amount > 10000 or amount < 100:
                print("Sorry the amount is too much , You can deposit below 10 thousand and above 100")
            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount has been deposited successfully")

    def Withdrawmoney(self):
            accnumber = input("Enter your account number :")
            pin = int(input("Enter your pin aswell :"))
    
            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
    
            if userdata == False:
                print("No such account exist")
            else:
                amount = int(input("Enter the amount you want to Withdraw :"))
                if userdata[0]['balance'] < amount:
                    print("Sorry , You don't have enough balance to withdraw")
                else:
                    print(userdata)
                    userdata[0]['balance'] -= amount
                    Bank.__update()
                    print("Amount has been withdrew successfully")

    def Showdetails(self):
            accnumber = input("Enter your account number :")
            pin = int(input("Enter your pin aswell :"))

            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

            print("YOUR ACCOUNT INFORMATION ARE :")
            for i in userdata[0]:
                print(f"{i}:{userdata[0][i]}")

    def UpdateDetails(self):
            accnumber = input("Enter your account number :")
            pin = int(input("Enter your pin aswell :"))
        
            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

            if userdata == False:
                print("No such account exist")

            else:
                print("You cannot change the age,account number,Balance")

                print("Fill the details for change or leave it empty if no change is required")

                newdata = {
                    "name": input("Enter your new name or Press ENTER"),
                    "email": input("Enter your new email or Press ENTER"),
                    "pin":  input("Enter your new pin or Press ENTER")

                }

                if newdata["name"] == "":
                    newdata["name"] = userdata[0]["name"]

                if newdata["email"] == "":
                    newdata["email"] = userdata[0]["email"]

                if newdata["pin"] == "":
                    newdata["pin"] = userdata[0]["pin"]

                newdata["age"] = userdata[0]["age"]

                newdata["accountNo."] = userdata[0]["accountNo."]

                newdata["balance"] = userdata[0]["balance"]

                if type(newdata["pin"]) == str:
                    newdata["pin"] = int(newdata["pin"])

                for i in newdata:
                    if newdata[i] == userdata[0][i]:
                        continue
                    else:
                        userdata[0][i] = newdata[i]
                Bank.update()
                print("Your details has been updated successfully")

    def Deleteaccount(self):
            accnumber = input("Enter your account number :")
            pin = int(input("Enter your pin aswell :"))

            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

            if userdata == False:
                print("No such account exist")

            else:
                check = input("Are you sure you want to delete your account ? (Y/N) :")
                if check == "N" or check == "n":
                    print("Bypassed")

                else:
                    index = Bank.data.index(userdata[0])
                    Bank.data.pop(index)
                    print("Your account has been deleted successfully")
                    Bank.update()
                 




user = Bank()
print("Press 1 for Creating a Account")
print("Press 2 for Depositing the Money in the bank")
print("Press 3 for Withdrawing the Money from the bank")
print("Press 4 for Details")
print("Press 5 for Updating Details")
print("Press 6 for Deleting the Account")

check = int(input("Tell your Response :"))

if check == 1:
    user.Createaccount()

if check == 2:
    user.Depositmoney()

if check == 3:
    user.Withdrawmoney()

if check == 4:
    user.Showdetails()

if check == 5:
    user.UpdateDetails()

if check == 6:
    user.Deleteaccount()