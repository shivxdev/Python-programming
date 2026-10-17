""" TUPLE -: immutable,duplicate,heterogenous,ordered"""

a = (1,2,3,4,5,5,5,5)

for i in range(len(a)):
    print(a[i])

#Methods of Tuple

index = a.index(5) #Find the index of first occurence of 5
print(index)

count_5 = a.count(5) #To count occurences of 5 
print(count_5)

l,m,n,o,p = (9,8,7,6,5) #unpacking 

print(m)

#if single element in the tuple then useb"," after one data otherwise it will give integer type 
z = (1,)

