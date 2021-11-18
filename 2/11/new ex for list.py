

# write a program that ask the user to fill a list with n names 
# then output the list after removing the repeated names and capitalize them


nameslist=[]
n=int(input("enter n:"))
newlist=[]

for i in range(n):
    name=input("enter name "+str(i+1)+":")
    nameslist.append(name)

#     newlist.append(name.capitalize())

# print(newlist) 
# for j in newlist:
#     if newlist.count(j)>1:
#         newlist.remove (j)  
# print(newlist)

for i in range(len(nameslist)):
    nameslist[i]=nameslist[i].capitalize()
print("after int:",nameslist)

for x in nameslist:
    if x not in newlist:
        newlist.append(x)
print("after removing:",nameslist)

      
    
    