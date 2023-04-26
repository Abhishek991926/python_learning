# using function print the fibbonacci series :

def fibonacci_series():
    n=int(input("enter the numbers :"))
    x=0
    y=1
    z=0
    while(z<=n):
        print(z)
        x=y
        y=z
        z=x+y
fibonacci_series()        