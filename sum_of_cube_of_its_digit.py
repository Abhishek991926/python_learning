# python program to find sum of cube of its digit 

n=int(input("enter the numbers :"))

sum=0

while(n>0):

    sum+=(n%10)*(n%10)*(n%10)

    n=n//10

print("sum of cube of its digit = ",sum)    