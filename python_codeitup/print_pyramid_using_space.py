# python program to print pyramid using space :

n=int(input("enter the numbers :"))
i=1
while(i<=n):
    b=1
    while(b<=n-i):
        print(" ",end="")
        b+=1
    j=1
    while(j<=i):
        print("*",end="")
        j+=1
    print()
    i+=1
