
import random

word=["apple","banana","cars","mickey"]
wordi = list(word)
empty = []
for g in range(len(word)):
    empty.append("-")

s=len(word)
correctword=[]
e=7
while e > 0:
    letter=input("guess a letter:")
    if letter not in word:
        print("wrong")
        e=e-1
    else:
        print("correct")
    if letter in word:
        correctword.append(letter)
        k = wordi.index(letter)
        empty[k] = letter
        word.remove(letter)
        if len(correctword) ==s:
            for h in empty:
                print(h,end="")
            print("")
            print("you win")
            break
if e==0:
    print("you lose")









       

