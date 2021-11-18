
#write a while/for loop to calculate the sum of the integers between n & m ,
# note that N is the first number in the series and M is the last number 
# EX:N22, enter M:26 
# the sum of 22+23+24+25+26=120


n=int(input("enter N :"))
m=int(input("enter M :"))
i=n
sum=0
print("the sum of ",end="")#byfselon bi space mabynzal 3l sater
while(i<m):
    sum=sum+i
    print(i,end="+") #bidalo 3a nafs lsater
    i=i+1
sum=sum+m
print(m,"=",sum)



#write a while/for loop to calculate the sum of the integers between n & m ,
# note that N is the first number in the series and M is the last number 
# EX:N22, enter M:26 
# the sum of 22+23+24+25+26=120
# the sum of 22+24+26+28+30=...

# n=int(input("enter N :"))
# m=int(input("enter M :"))
# i=n
# sum=0
# while(i<=m):
#     sum=sum+i

#     i=i+2#hon +2



#tari2a teniye
# n=int(input("enter N :"))
# m=int(input("enter M :"))
# i=n
# sum=0
# print("the sum of ",end="")#byfselon bi space mabynzal 3l sater
# while(i<m):
#     sum=sum+i
#     if(i==m):
#         print(i,end="") #bidalo 3a nafs lsater
#     else:
#         print(i,end="+")
#     i=i+1
# sum=sum+m
# print(m,"=",sum)
