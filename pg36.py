#1. Print all positive and negative elements of list

a = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]

print("The positive elements of list are:")
for i in a:
    if i>=0:
        print(i)
print("The negative elements of list are:")
for i in a:
    if i<=0:
        print(i)

#2. Mean of list element

b =[12,13,14,15,21,22,23,24,25]
sum=0
for i in b:
    sum = sum+i

print(f"The mean of the list is {sum/len(b)}")

# 3. Largest element in the list 

c = [12,123,1234,12345,123456,1234567,12345678]

largest = c[0]
index = 0

for i in range(len(c)):
    if c[i] > largest:
        largest = c[i]
        index = i

print(f"Your largest number is {largest} at Index {index}")

#4. Find the second largest number in the list 

d = [11,22,33,44,55,45]

largest =  d[0]
sec_largest = d[0]

for i in d:
    if i > largest:
        sec_largest = largest
        largest = i 
    elif i > sec_largest:
            sec_largest = i

print(f"The second largest number is {sec_largest}")


#5 . sort the element of list 

x = [10,14,18,22,26,30]

for i in range(len(x)-1):
   if x[i] < x[i+1]:
      continue
   else:
      print("your list is not sorted")
      break
else:
   print("Your list is sorted")