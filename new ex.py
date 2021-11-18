

#write a while /for loop to checks 5 numbers if they are even or odd

# i=0
# while(i<=5):
#     num=int(input("enter a num :"))
#     if (num%2==0):
#         print("the num is even")
#     else:
#         print("the num is odd")
#     i=i+1



#write a while /for loop to checks 5 numbers if they are even or odd and badna n3edon
# i=0
# odd=0
# even=0
# while(i<=5):
#     num=int(input("enter a num :"))
#     if (num%2==0):
#         print("the num is even")
#         even=even+1
#     else:
#         print("the num is odd")
#         odd=odd+1
#     i=i+1
# print("num of odd",odd)
# print("num of even",even)






#write an alarm app that awake a person at a predefined time set by him, 
# if he doesn't want to get up,
# let him set the alarm to snooze which means he will postpone the alarm 5 minutes or more,
# repeat this process till the person wake up

a=input("set an alarm at :")
print("gonna to wake u up",a)
b=input("snooze or close ?")
while(b=="snooze"):
    print("its time to wake up")
    c=input("snooze or close")
    if(c=="close"):
        print("alarm off")
        break
else:
    print("alaram off")