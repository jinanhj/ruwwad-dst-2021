#write a program that ask the user to enter the names and the grade
#of the students in two lists
#then output the name and grade of each students

# name=["ahmad","samir","ali","marie","hassan"]
# grade=[20,23,40,100,50]

# # print(name,grade)
# # print(name[1])#eza bdi 3ayet la esm mou7adad
# # print(name[0:2])
# for i in range(len(name)):
#     print(name[i]+"\t",grade[i])#\t mshen tertib


#write a program that ask the user to enter the names and the grade
#of the students in two lists
#then output the name and grade of each students

students=["ahmad","samir","ali","marie","hassan"]
grade=[20,23,40,100,50,20,60]
students.append("jinan")#betzid kelme e5er list
students.insert(1,"maysa")#btzedli kelme 7asab wen ana badi nyeha
students.extend(grade)#btedmoj 2 lists
# for i in range(len(students)):
#     print(students[i]+"\t",grade[i])
print(students)

