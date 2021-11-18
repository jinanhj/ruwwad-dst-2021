name=[]#empty list
# names1=liste(())
nb_cars=int(input("enter the nb of cars:"))
for i in range (nb_cars):

    car_name=input("enter the name of the car:")
    while car_name in name:
       car_name=input("error,duplicate cars, enter a new car:")

    else:
        name.append(car_name)
        # names1.insert(2,car_name)

print(name)#will output the element of the liste....
for i in range(len(name)):
    print(name[i],end="-")





# names=["hassan",12,True,"hassan"]#name[0]=>"hassan"
# numbers1=liste((12,18,22))

# nbs=[12,22,44]
# names[1]=14#te8yiiir
# names[4]="ali #error index out of range"



# grades=[]



