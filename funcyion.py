#write a function called averge that takes N numbers as a parameter and returns the avarege of the numbers

# def averge(*number):
#     sum=0
#     for i in range(len(number)):
#         sum=sum+number[i]
#     aver=sum/(len(number))
#     print("valeur moyen =",aver)
  
# averge(11,14,15)



def averge(n):
    sum=0
    for i in range(n):
        nb=int(input("enter a number:"))
        sum=sum+nb
    aver=sum/n
    print(aver)
n=int(input("enter n:"))
  
averge(n)