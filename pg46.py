""" OOPS constructor"""

class Factory:
    def __init__(self,material,zips,pockets):
        
        self.material = material 
        self.zips = zips
        self.pockets = pockets
    def show(self):
        print(f"your object details are {self.material},{self.zips},{self.pockets}")

rebook = Factory("leather",3,2)

campus = Factory("nylon",5,3)

# print(campus.pockets)

rebook.show()