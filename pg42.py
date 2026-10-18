"""FILE HANDLING"""

o = open(r'C:\Users\ssshi\OneDrive\Desktop\srishti\index.html')

print(o.read())

c = open("pg43.py",'w') #To create file in file handling using 'w'

#To write something in the file 

c.write("Hello this is shivam and i am writing inside this file ") #Lekin ye ky krta hai ki overwrite krta hai like agr hamne ek baar kuch likha then fhir se kuch likha toh phle wala htt jata hai 

c.close()

#toh overwrite wali problem ko hatane ke liye ham write'w' ki jgh append'a' use kr skte hai 

c = open("pg43.py",'a') #To create file in file handling using 'w'

#To write something in the file 

c.write("and now i am appending some text ") #Lekin ye ky krta hai ki overwrite krta hai like agr hamne ek baar kuch likha then fhir se kuch likha toh phle wala htt jata hai 

c.close()

"""   'r' -: read
      'w' -: write
      'a' -: append
      'x' -: only create (fails if file already exist)  """
