
# newliste=["banana","orange","lemon"]
# newliste=[x if x != "banana" else "orange" for x in newliste]

# print(newliste)


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")#btmhi shi eza kn mawjoud
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)#btm7i shi m7adad fonction
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()#eza msh m7adad ra7 ye5od e5er shi maktoub
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist# bem7i kl liste


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()#betfadi element li jouweta liste
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1



A=[1,2,3,4,5]
B=[10,9,8,7,5]
c=[]

for i in range (len(A)):
    sum=A[i]+B[-i-1]
    c.append(sum)
 
print(c)
