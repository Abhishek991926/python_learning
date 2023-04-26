# program two find max of three numbers :

num1=int(input("enter the first numbers :"))

num2=int(input("enter the second numbers :"))

num3=int(input("enter the third numbers :"))

if (num1>num2)&(num1>num3):

    print("max number is =",num1)

elif(num2>num1)&(num2>num3):

    print("max number is =",num2) 

else:

    print("max number is =",num3)       