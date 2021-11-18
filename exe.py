#write the program that asks the user if the weather is good or not,
#if it is good then ask if he would like to play football or he can go for a walk,otherwise he should stay at home

# a=input("how is the weather today [good or bad] ?")
# if a=="good":
#     b=input("would you like to go for a walk or play football")
#     if b=="no":
#        print("i hate you")
#     else:
#            print("lets goo")
# else:
#     print("stay at home")


  
w=input("is weather good ? ")
if w=="yes":
    f=input("do u play football ?")
    if f=="yes":
        print("nice")
    else:
        walk=input("walk ?")
        if walk=="yes":
            print("nice")
        else:
            print("stay at home and enjoy the weather")
else:
    print("stay at home the weather not good")
            
    