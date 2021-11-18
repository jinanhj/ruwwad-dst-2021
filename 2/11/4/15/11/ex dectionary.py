# Farm = { “Cats”: 10, “Dogs”: 7, “Cows”: 5, “Horses” : 1}
# • How to get the number of cats?
# • How to get a list of all the animals in the farm?
# • How to check if there is a hen in the farm?
# • 2 dogs are to be added to the farm. How to do this?
# • A new rabbit is to be added to the farm. How to do this?
# • The horse died and so no more horses are in the farm. How to 
# remove the horse?
#  How to get the total number of animals in the farm?
# • How to get the number of distinct animals in the farm?
# • How to get the animal that is the most existing in the farm?


Farm = { "Cats": 10, "Dogs": 7, "Cows": 5, "Horses" : 1}
print("\n the number of cats is:", Farm ["Cats"])

print("\n a \n list of all the animals in the farm is:",Farm.keys())

print("\n check if there is a hen in the farm","hen" in Farm)

Farm["Dogs"]=Farm["Dogs"]+2
print("\n add 2 dogs to the farm:",Farm["Dogs"])

Farm["rabbits"]=1
print(Farm)

Farm.pop("Horses")
print(Farm)

sum=0
for i in Farm:
    sum=sum+Farm[i]
print("\n the total number of animals in the farm is:" ,sum)

print("\n the number of distinct animals in the farm is:",Farm.values())

# • How to get the animal that is the most existing in the farm?
m1=max(Farm.values())
for x in Farm:
    if Farm[x]==m1:
        print("\n the animal that is the most existing in the farm is :",x)




# • How to get the animal that is the most existing in the farm?
# for x in Farm.keys():#print(farm.keys())
#     print(x,end=" ")
# x1=[x for x in Farm.keys()]

# for x in Farm.values():#print(farm.values())
#     print(x,end=" ")