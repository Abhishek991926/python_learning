# python program to check the given numbers is palindrome or not 


n=int(input("enter the numbers :"))

i=n
rev=0
while(i>0):
    rev=(rev*10)+(i%10)

    i=i//10

if(rev==n):
    print("palindrome number ")
else:
    print("not palindrome number ")        