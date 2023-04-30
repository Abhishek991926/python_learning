# write a program to find sum of square of naturals numbers :

n=int(input("enter the numbers : "))

i=1

sum=0

while(i<=n):
    sum+=i*i
    i+=1

print("sum of square =",sum)    