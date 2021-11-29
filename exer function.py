
# 1.write a python function to find and return the max of three numbers

# 2.write a python function to sum all the number in a list without using the sum function.
# samle list:(8.2.3.0.7)
# expected output:20

# 3.write a python program to reverse string
# sample string:"1234abcd"
# expected output:"dcba4321"

# 4.write a python function to calculate the factorial of a number (a non-negative integer).
# the function accepts the number as an argument.
# ex:6!6*5*4*3*2*1
# 0!=1


#1)

# def max_of_three_numbers( a,b,c ):
#     if (a > b  and a > c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#             return c
# x1=int(input("enter a number:"))
# x2=int(input("enter a number:"))
# x3=int(input("enter a number:"))    
# print("max_is:", max_of_three_numbers(x1,x2,x3))



#2)
					

# l1 = [8,2,3,0,7]
# def sumlist(l1):
#     sum = 0
#     for i in l1:
#         sum=sum+i
#     return(sum)

# print(sumlist(l1))



#3)

# def reverse(word):
#     s=""
#     for i in range (len(word)-1,-1,-1):
#         s=s+word[i]
#     return(s)

# print("reversed string:",reverse("jinan"))


# def reverse(word):
#     return word[::-1]
# word="ahmad"
# print(reverse(word))


#4)

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
number=int(input("Input a number to compute the factiorial : "))

print(factorial(number))



