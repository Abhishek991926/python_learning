# python program to print sum of even numbers from 1 to n 

# where n is provided by users :

n=int(input("enter the numbers : "))

i=2

sum=0

while(i<=n):

    sum+=i

    i+=2

print("sum of even numbers = ",sum)    


# method 2nd 


n1=int(input("enter the numbers :"))

i=1

sum=0

while(i<=n1):

    if(i%2==0):
        sum+=i
    i+=1
print("sum of even numbers =",sum)        