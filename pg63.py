"""List , dictionary and set comprehension"""
#Comprehension of list 

#Basically multiple line of code in a single line 

l = []
for i in range(1,21):
    if i%2 == 0 :
        l.append(i)

print(l)

l = [i for i in range(1,21) if i%2 == 0]     #This is comprehension 

print(l)

