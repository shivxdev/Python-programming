d = [11,22,33,44,55]

largest =  d[0]
sec_largest = d[0]

for i in d:
    if i > largest:
        sec_largest = largest
        largest = i 
    elif i > sec_largest:
            sec_largest = i

print(f"The second largest number is {sec_largest}")

empty_dict = {}
empty_set = set()

print(type(empty_dict),type(empty_set))