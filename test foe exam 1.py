#write a program that asks the user to enter his gender , and his age, if his age is above 20 and he is a man,
# output his age and say "you can play football", if his age is below 20,he can't play football,
#otherwise tell the girl to play basketball


#write a program that accepts a string of five caracteres and calculate the number of digits and letters
 

# gender=input("enter your gender M or F:")
# age=int(input("enter your age :"))

# if (age>20 and gender=="M"):
#   print("you can play football")
# elif (age<20 and gender=="M"):
#     print("you can't play football")
# else:
#      print("go to play basketball")


# five=input("enter a string of 5 caracters:")


# if len(five)>5:
#     print("pay attention of the nb of carac:")


# if len(five)<5:
#         print("oum 7el 3anna")
# else:
#     f0=five[0]
#     f1=five[1]
#     f2=five[2]
#     f3=five[3]
#     f4=five[4]

#     digits=0
#     letters=0

# if f0.isalpha():
#     letters=letters+1
# elif f0.isdigit():
#     digits=digits+1

# if f1.isalpha():
#     letters=letters+1
# elif f1.isdigit():
#     digits=digits+1

# if f2.isalpha():
#     letters=letters+1
# elif f2.isdigit():
#     digits=digits+1

# if f3.isalpha():
#     letters=letters+1
# elif f3.isdigit():
#     digits=digits+1


# if f4.isalpha():
#     letters=letters+1
# elif f4.isdigit():
#     digits=digits+1

# print("nb of letters:",letters,"nb of digits",digits)




nb=0
letters=0
digits=0

while(nb<len(name)):
    if(name[nb].isalpha()):
        letters=letters+1
    elif(name[nb].isdigt()):
        digits=digits+1
  nb =nb+1
 print("the num of lett:",letters)
 print("the num of dig:",digits)




