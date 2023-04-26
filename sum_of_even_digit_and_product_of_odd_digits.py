# python program to find the sum of even digit and product of odd digits :

n=int(input("enter the numbers :"))
sum=0
pro=1
while(n>0):
    d=n%10
    if(d%2==0):
        sum+=d
    else:
        pro=pro*d
    n=n//10  
print("sum of even digit= ",sum) 
print("product of odd digit= ",pro)         