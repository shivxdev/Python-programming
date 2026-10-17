"""SETS-: mutable , not duplicate , sets are unordered and we cannot access them through index value 
 SEMI-HETROGENOUS -: we can store different data types but not everything """

s = {1,2,3,4,5,6,7,8,9}
print(s)

#METHODS -:
#1. To add an element in set 
s.add(10)
print(s)

#2. To remove something from set 
s.remove(10)
print(s)

#3 . to remove element (no error if not found)
s.discard(100)
print(s)

#4. Removes random element from the set
popped_element = s.pop()
print(popped_element)
print(s)

#5. To remove all element from set
s.clear()
print(s)

"""SOME OPERATIONS BW TWO SETS"""

A = {1,2,3}
B = {3,4,5}

# union of two set
union_set = A.union(B)
print(union_set)

#intersection of two set
intersection_set = A.intersection(B)
print(intersection_set)

#Difference of two set
diff_set = A.difference(B)
print(diff_set)

#symmetric difference
sym_diff = A.symmetric_difference(B)
print(sym_diff)