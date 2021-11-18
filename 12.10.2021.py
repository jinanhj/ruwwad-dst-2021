#etba3 5 numbers
# i=1 #ini
# while(i<5):#conditi
#     print(i)
#     i=i+1


#asks the user to print num between 1 and N

# i=1
# n=int(input("enter a number:"))
# while(i<=n):
#     print(i)
#     i=i+1



#write the program that asks the user to enter 5 numbers then calculate the number of positive numbers

# i=0
# p=0
# while (i<5):
#     nb=int(input("enter the number positive :"))
#     if(nb>=0):
#         p=p+1
#     i=i+1
#     print("the nb of positive numb:",p)

#write the program that asks the user to enter 5 numbers then calculate the number of positive numbers and positive
# i=0
# positivenum=0
# negativenum=0
# while (i<5):
#     nb=int(input("enter the number :"))
#     if(nb>=0):
#         positivenum=positivenum+1
#     else:
#         negativenum=negativenum+1
#     i=i+1
#     print("the nb of positive numb:",positivenum) 
#     print("the nb of negative numb:",negativenum)



#write the program that asks the user to enter 5 numbers positive then calculate the number of positive numbers and positive
# i=0
# positivenum=0
# negativenum=0
# while (i<5):
#     nb=int(input("enter the number :"))
#     if(nb>=0):
#         positivenum=positivenum+1
#     else:
#         negativenum=negativenum+1
#         i=i+1
#     print("the nb of positive numb:",positivenum) 
#     print("the nb of negative numb:",negativenum)





#write a python program that asks the user to enter three variable then output the biggest one


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
  biggest = num1
elif (num2 > num1) and (num2 > num3):
   biggest = num2
else:
   biggest = num3

print("The biggest number is",biggest)



