"""Object oriented programming"""

class Factory:

#There are two types of things inside the class  1.ATTRIBUTE  2.METHODS 


 #variable define inside the class are ATTRITUBE 
    brand = "Strong steel"

 #function define inside the class are METHODS

    def hello(self):
        print("How are you")
   

#to access attribute
print(Factory().brand)

#to call method
Factory().hello()

obj = Factory()  #Object created