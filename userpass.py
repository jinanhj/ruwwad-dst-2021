#write a program that asks the user to login to his account.
#if his username or password is incorrect<you can display a login error otherwise display login successfully

dusername="jinan"
dpassword="123"

username=input("enter your username:")
password=input("enter your password:")
if (username==dusername):
    if(password==dpassword):
        print("login successfully")
    else:
      print("incorrect password")
else:
 print("incorrect username/login faild")

   




