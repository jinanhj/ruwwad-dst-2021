# create a list called mylist with the following six items:76.96.3"hello,true 4,76
# begin with the empty list shown below,and add 6 statements to add each
# item, one per item.the first three statements should use the append method to
# append the item to the list,and the last three statements should use concatenation

# write python statements to do the following:

# a.append"apple" and 76 to the list.append
# b.insert the value"cat" at position 3
# c.insert the value 99 at  the start of the liste
# d.find the index of "hello"
# e.count the number of 76s in the list
# f.remove the first occurrence of 76 from the liste
# g.remove true from the list using pop and index

mylist=[]
mylist.append(76)
mylist.append(96.3)
mylist.append("hello")
mylist=mylist + [True]
mylist=mylist + [4]
mylist=mylist + [76]
print(mylist)

mylist.append("apple")
mylist.append(76)
print("append apple and 76",mylist)

mylist.insert(2,"cat")
print("insert cat at position3:",mylist)

mylist.insert(0,99)
print("insert 99 at the beginning:",mylist)

mylist.index("hello")
print("find the index of hello is:",mylist.index("hello"))
print("the number of 76s is:",mylist.count(76))

mylist.remove(76)
print("remove the first 76",mylist)
mylist.pop(mylist.index(True))
print("remove true:",mylist)





