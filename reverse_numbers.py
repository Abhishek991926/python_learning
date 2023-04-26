# python program to print the reverse numbers 


n=int(input("enter the numbers :"))

rev=0
while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10

print("rev of number =",rev)    