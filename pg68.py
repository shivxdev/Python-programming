"""FILTER"""

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = filter(even,a)
print(list(result))

res =filter(lambda x: True if x % 2 == 0 else False,a )
print(list(res))