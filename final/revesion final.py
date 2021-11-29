# write a python program to convert two lists into a dictionary in a way that item 
# from list1 is the key and item from list2 is the value
# names=["salim","joud","katia"]
# ages=[15,40,22]
# output:dict={"salim":15,"joud":40,"katia":22}




names=["salim","joud","katia"]
ages=[15,40,22]

print("List1 : ", names)
print("list2 : ", ages )

# a = {}

# # COnvert to dictionary
# for key in names:
#    for value in ages:
#       a[key] = value
#       ages.remove(value)
#       break
# print("Dictionary from lists :\n ",a)

dict1={}
for i in range (len(names)):
   dict1[names[i]]=ages[i]
print(dict1)