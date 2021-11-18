# *
# **   
# ***  
# **** 
# *****


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")



# *****
# ****
# *** 
# **  
# *

# for i in range(1,6):
#     for j in range(0,6-i):
#         print("*",end="")
#     print("")


#another method for

# *****
# ****
# *** 
# **  
# *



for i in range (5,0,-1):
    for k in range (1,i+1):
        print("*",end="")
    print()




# ----*
# ---*
# --*
# -*
# *

# for i in range(1,6):
#     for j in range(0,5-i):
#         print("-",end="")
#     print("*")



#        * 
#       * * *     
#     * * * * *   
#   * * * * * * * 
#       * * *     
#       * * *


for i in range (1,8,2):
    print(" "*(3-int(i/2)),"*"*i)

print("  ",3*"*")
print("  ",3*"*")



#         * 
#       * * *     
#     * * * * *   
#   * * * * * * * 
#       * * *     
#       * * *

# for i in range (1,5):
#     a=" *"*i
#     b=4-i
#     d="* "*(i-1)
#     print("  "*b,a,d)
# for w in range(1,3):
#     print("      * * *")



#        * 
#      * * *     
#    * * * * *   
#  * * * * * * * 
#      * * *     
#      * * *

# for i in range (1,8,2):
#     s=" "
#     s=s*(7-i)
#     print(s,"* "*i)
# print("     * * *")
# print("     * * *")
