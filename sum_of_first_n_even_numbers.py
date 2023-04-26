# program to find the sum of first n even numbers :

n=int(input("enter the numbers :"))

i=1

sum=0

count=0

while(count<n):

    if(i%2==0):
        sum+=i
        count+=1

    i+=1

print("sum of n even numbers =",sum)        