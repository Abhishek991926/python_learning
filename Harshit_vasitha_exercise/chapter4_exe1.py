# define a function that take two numbers and return greter of the numbers :

def greter_num(a,b):
    if a>b:
        return a
    return b
x=int(input("enter the first numbers :"))
y=int(input("enter the second numbers :"))
print(f"Greter number: {greter_num(x,y)}")