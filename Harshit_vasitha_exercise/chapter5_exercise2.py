# define a function which will take list as a argument and this function return reversed of the list :

#[1,2,3,4].>>>>[4,3,2,1]

def rev_list1(l1):
    rev_list2=[]
    for i in range(len(l1)):
        d=l1.pop()
        rev_list2.append(d)

    return rev_list2

l3=list(range(1,int(input("enter the range you want :"))))
print(l3)
print(f"reverse list :{rev_list1(l3)}")    