# python program to find sum of digit of a given numbers :

n=int(input("enter the numbers :"))

i=n

sum=0

while(i>0):

    sum+=i%10

    i=i//10

print("sum of digit = ",sum)




    