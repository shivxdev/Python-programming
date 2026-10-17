"""PROGRAM ON DICTIONARY"""

d1 = {1:10,2:20,3:30}
d2 = {4:40,5:50,6:60}

d1.update(d2) #Method 1 

print(d1)

for i in d2:
    d1[i] = d2[i] #Method 2

print(d1)

#Q.1 sum of all values in dict 
d = {1:100,2:200,3:300,4:400}
sum = 0

for i in d.values():
    sum = sum+i
print(f"The sum of all values of dict is :{sum}")


#Q3 ..count the frequency of each element 

l = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6]

def count(a):  #method 1 using function 
    total = 0
    for i in l:
        if i == a:
            total = total + i

    print(f"The frequency of {a} is {total}")

count(1)



for a in set(l):  #Mehod 2 using function 
    total = 0
    for i in l:
        if i == a:
            total += 1

    print(f"The frequency of {a} is {total}")


#Method 3 by using dictionary method

d = {}
for i in l:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1

print(d)