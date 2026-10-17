"""DICTIONARY -: mutable,Duplicates(keys must be unique ...values can be duplicate),heterogenous,ORDER = follows insertion order """

d = {1:"hello"}

print(d[1]) # way  of accessing 

student = {"Name":"Shivam","Age":19}

print(student["Name"])

m = {10:100,20:200,30:300,40:400}

m[10] = 1000 #updating values of key 
print(m)

m.update({50:500}) #adding key and value in the dict
print(m)

for i in m:
    print(i) # for accessing keys 

for i in m:
    print(m[i]) # for accessing values of key 

#2nd type to access the values

for i in m.values():
    print(i)

 #DEEEP COPY CONCEPT 
r = [1,2,3,4,5]

s = r

s[0] = 100

print(r)

#SHALLOW COPY CONCEPT
u = {1:10,2:20,3:30,4:40,5:50}

v = u.copy()

print(v)
