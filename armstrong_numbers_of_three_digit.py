#  python program to print armstrong numbers of 3 digit 

n=int(input("enter the numbers :"))

temp=n

sum=0

while(n>0):

    sum+=(n%10)*(n%10)*(n%10)

    n=n//10

if(sum==temp):

    print("Armstrong") 
else:

    print("Not armstrong")       