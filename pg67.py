#To print the double of each number in a list using map and lambda function

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2,numbers)

print(list(result))

def double(x):
    return x * 2
                              #second way to print the double of each number in a list using map and function
res = map(double,numbers)

print(list(res))

