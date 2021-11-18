#write a python program as a function that determines the union of two sets without using any predefined functions.


e={"lenovo","hp","del","accent","asus"}
f={"acer","thomson"}
def unionset():
    for x in e:
        f.add(x)
    return f

print(unionset())







