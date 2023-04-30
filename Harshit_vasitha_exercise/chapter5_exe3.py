# define a function that will take list of words as a argument and 
# return list with reverse of every element :
# example ["abc","tuv","xyz"]>>>>>["cba","vut","zyx"]


def rev_list1(l1):
    r_list=[]
    for i in range(len(l1)):
        r_list.append(l1[i][::-1])
    return r_list

l2=["abhishek","shivani","moni","neeraj"]
print(rev_list1(l2))


