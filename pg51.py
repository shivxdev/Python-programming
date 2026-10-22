"""CONSTRUCTOR IN MULTIPLE INHERITANCE"""

# multiple inheritance

class glass:
    # material1 = "water"
    def __init__(self,name):
        pass

class glass2:
    # material2 = "softdrink"
    def __init__(self,name,age):
        pass

class glass3(glass,glass2):  #child can contain multiple parent
    material3 = "both"

 obj = glass3()  #The constructor function will be inherited of the first class that has been inherited . This is mro ( method of resolution)

#multilevel inheritance padhna hai basically usme grand parent > parent > child 
