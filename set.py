# write a program to define a set :
# 1-add three elements to the set
# 2-print the elements to the set
# 3-update the set with two new elements from a list
# 4-ask the user to remove N elemenets from the set
# 5-ask the user whether he wants to clear or remove the set then print it

thiset=set(())
for i in range (3):
    n=input("enter a number:")
    thiset.add(n)
print(thiset)

mylist=[5,6]
thiset.update(mylist)
print(thiset)

a=int(input("remove N element:"))
for i in range(a):
    thiset.pop()
print(thiset)

b=input("you want to clear or remove the set:")
if b=="clear":
    thiset.clear()
    print(thiset)
else:
    del thiset
    print(thiset)
