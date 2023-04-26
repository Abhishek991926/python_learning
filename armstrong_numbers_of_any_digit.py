# python program to find armstrong numbers of any digit :

n=int(input("enter the numbers :"))

i=n

count=0

while(i>0):
    count+=1
    i=i//10

print('count',count)

sum=0
i=n
while(i>0):
    digit=i%10

    sum += digit**count
    i=i//10


if(sum==n):
    print("armstrong")
else:
    print("not armstrong")              