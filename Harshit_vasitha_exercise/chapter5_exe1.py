# define a function which will take list containing numbers as a input 
# amd return the list containing square of every element :

def square_list(l):
    square_list1=[]
    for i in l:
        square_list1.append(i*i)
    return square_list1


l2=list(range(1,int(input("enter the range you want :"))))
print(l2)
print(square_list(l2))        