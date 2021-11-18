birthdays={}
ans="yes"
while ans=="yes":
    name=input("enter a name:")
    bday=input("enter a birthday:")
    if name not in birthdays:
        birthdays[name]=bday
    else:
        print("that entry already exists:")
    print("\n the birthdays dictionary contains:",birthdays)#\n nezel 3a new ligne
    ans=input("\n add another entry? (y for yes)")
print("\n name \t\t birthdays")#3meli kaza espace
print("----------------------------------------")
for name in birthdays:
    print(name,"\t\t",birthdays[name])
del birthdays[ali]