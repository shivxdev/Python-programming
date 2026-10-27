"""ARGS AND KWARGS"""
#args -  argument

def addition(*args):
    sum = 0
    for i in args:
        sum = sum+i

    print(f"The total sum is {sum}")
                   #For inputting multiple inputs  multiple inputs isliye aa jate h kyuki wo tuple form create kr eta hai 
addition(12,12,23,56,89,97,66,47,86)