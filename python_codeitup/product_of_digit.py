# python program to find the product of digit of a given numbers :

n=int(input("enter the numbers :"))

pro=1
while(n>0):
    pro=(n%10)*pro

    n=n//10

print("product of digit =",pro)    