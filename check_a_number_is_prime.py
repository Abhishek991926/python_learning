# python program to check a number is prime or not 


n=int(input("enter the numbers "))

i=1
count=0
while(i<=n):
    if(n%i==0):
        count+=1
    i+=1
print(count)
if(count==2):
    print("numbers is prime")
else:
    print("number is composite")            
