# ask user name and age if user name start "A","a" and age is above 10 watch coco movie 
# another user can not watch coco movie :

name=input("enter the user name ")
age=int(input("enter the age :"))
if ((name[0]=="A" or "a" )and age>10):
    print("watch coco movie ")
else:
    print("you can not watch coco movie ")    