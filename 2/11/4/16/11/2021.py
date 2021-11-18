
Participants = [{"First": "Tom", "Last" : "White", "Age" : 35} ,
{"First" : "Tedd", "Last" : "Smith", "Age" : 21},
{"First" : "Sarah", "Last" : "Lewis", "Age" : 40} ]

print("First \t Last \t Age")
print("--------------------")
for x in Participants:
    print(x["First"],"\t", x["Last"],"\t", x["Age"])