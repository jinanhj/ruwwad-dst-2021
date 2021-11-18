#write a program that asks the user then asks him to search for a letter in this phrase.if the letter exixts,then the program should print its number of occurrences.the letters are case sensitive



#1)
# phrase =input("enter a phrase:")
# letter = input("Enter a letter: ")
# while len(letter)>1:
#     letter = input("Enter a letter: ")

# nbrofoccurs = phrase.count(letter)
# if nbrofoccurs>0:
#     print("this letter occurs ",nbrofoccurs ,"time")




# for i in range (5,0,-1):
#     for k in range (1,10+1):
#         print("*",end="")
#     for j in range (1,2):
#         print(" ")
#     print()


# for row in range(1,6):
#     for col in range(1,11):
#         if (row==5 or row+col==5 or col-row==3):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# #2)





# k = 16
# tim = 1
# for i in range(0, 5):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 4
#     for j in range(0, tim):
#         print("* ", end="")
#     tim = tim + 2
#     print()




word=input("enter a word, phrase or number:")
while len(word)<2:
  word = input("enter a word, phrase or number: ") 
word= word.lower()  
listofpunctuation= [" ",",",";",".","?","!"]
for l in listofpunctuation:
  word = word.replace(l,'')
lenword = len(word)
reverseword=""
for i in range(0,lenword):
  reverseword += word[lenword-1-i]
  print(reverseword)
  if reverseword==word:
    print("it is a palindrom")
  else:
    print("it is not a palindrom")
 




#for i in range(0,5):
  #  for j in range(0,2):
   #     print((4-i)" "+(i+1)"*",end="")
   # print()