#1)
#  name=input("enter your name:")
# # print(name.replace("ya","ja"))
# # print(name.find("s"))
# print(name.isalnum())#eza num et alpha

# 2)
#10---->14
# c=10
# while(c<15):
#     print(c)
#     c=c+1

#3)
# for i in "Ahmad":
#     print(i)

#4)
# for i in range(6):
#     for j in range(6):
#         print(i,end="")
#     print()


#5)

# 000000
# 012345  
# 0246810 
# 03691215
# 048121620
# 0510152025


#6)

# for i in range(6):
#     for j in range(6):
#         print(i*j,end="")
#     print()


#7)

# for i in range(1,17):
#     if (i%4==0):
#         print(i)
#     else:
#         print(i,end="")

#8)
#write a program that asks the user to enter his name then print of time
#ex:enter your name:"ali"
#enter N=5

b=int(input("enter n:"))
while b>0:
    a=input("enter name:")
    c=len(a)
    for j in range(c):
        for i in range(-1,-c-1+j,-1):
            print(a[i],end=" ")
        print()
    b=b-1





#9)

# - - - * * * 
# - - + * * * 
# - + + * * *
# + + + * * *

# for i in range(1,5):
#     for j in range (1,5-i):
#         print("- ",end="")
#     for k in range (1,i):
#         print("+ ",end="")
#     for m in range (1,4):
#         print("* ",end="")
#     print()
    

#10)
# while true:
#     i =input("enter a name")
#     if i =="stop":
#         break
#     name= ""
#     for g in i:
#         name= g + name
#     print(name1)

