# using function print armstrong numbers :

def armstrong_numbers():
    n=int(input("enter the numbers "))
    i=n
    sum=0
    while(i>0):
        sum+=(i%10)*(i%10)*(i%10)
        i=i//10
    if(sum==n):
        print("armstrong numbers ") 
    else:
        print("not armstrong")       
armstrong_numbers()
