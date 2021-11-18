# write a program in python as a function that determines the intersection of two sets without using 
# any predefind function




lst1={"java","python","javascript","c #","c++"}
lst2={"VB.ET","java","kotlin","python"}

def intersection(lst1, lst2):
    lst3 ={x for x in lst1 if x in lst2}
    print(type(lst3))
    return lst3

print(intersection(lst1, lst2))
