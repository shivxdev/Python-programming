def palindrome(st):
    rev =""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st:
        print(f"The {st} is palindromic string")
    else:
        print(f"The {st} is not palindromic")

palindrome("naman")
palindrome("shivam")

def hey():
    return"Hey how are you"

print(hey())