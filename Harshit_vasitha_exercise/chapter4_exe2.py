# define a function and check the string is palindrome or not :

def is_palindrome(name):
    if (name==name[::-1]):
        return "palindrome"
    return "not palindrome"

string=input("enter the string : ")
print(is_palindrome(string))