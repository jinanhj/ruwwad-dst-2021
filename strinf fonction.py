name="hassan"
print(name.capitalize())#Hassan
print(name.startswith("ha",0,2))#true
print(name.startswith("ha",0,1))#false
print(name.startswith("ha"))#true
print(name.startswith("ha",0,4))#true
print(name.endswith("n",4,6))#true
names="Ali samir wali wali"
print(names.replace("wali","walid",1))
print(names.replace("youssef","walid",1))

a="1234xxc"
b="1234abc"
print(a.isalnum()) #true a7rof and number
print(a.isdigit())#false
print(a.lower())# true # a7rof z8ire true te7wil xxc
print(b.lower())#1234abc
print(b.upper())#1234ABC
print(a.upper())#XXC a7rof kbire
