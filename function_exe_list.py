
# #write a program the contains the following functions
# 1-a function to initialize a list of 10 integers
# 2-a function to print the element of the list
# 3-a function to remove an element from the list
# 4-a function to multiply by 2 the element of the list
# then print it

list1=[]

def initialize(list1):
    for i in range (10):
        a=int(input("enter a number:"))
        list1.append(a)
        print(list1)

def pl(list1):
    for j in list1:
        print(j,end=" ")

def re(list1):
    b=int(input("choose an element for remove:"))
    list1.remove(b)
    print(list1)

def multi(list1):
    for k in range (len(list1)):
        list1[k]=list1[k]*2
    print("after multiplication each number by 2:",list1)

initialize(list1)
pl(list1)
re(list1)
multi(list1)