# take a number and print the 1256 and print the sum of 1+2+5+6

num=int(input("enter the numbers :"))
sum=0
while(num>0):

    sum=sum+num%10
    num=num//10
print(f" sum of number is {sum}")    


num2=input("enter the numbers :")
i=0
sum=0
while len(num2)>i:
    sum+=int(num2[i])
    i+=1
print(f" sum of number is {sum}")    