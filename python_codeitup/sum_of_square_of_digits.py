# python program to find the sum of square of digits 

n=int(input("enter the numbers :"))

sum=0

while(n>0):

    sum+=(n%10)*(n%10)

    n=n//10

print("sum of square of digit =",sum)