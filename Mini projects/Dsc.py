
#while True:


 #  try:
  #  x=float(input("Enter 1st value:"))
   # y=float(input("Enter the 2nd  value:"))
    #username=input("Username")


    #print("Total:"+str(x+y))
   # print(username)
    
   #except ValueError:
   # print("Value must be an integer")




while True:
 username=input("Username:")
 if username=='morvin':
    passwd=input("Passcode:")
    if passwd=="4321" and len(passwd)==4:
       print("Login succesfull "+str(passwd.replace("4","morvin")))
       x="Ian morvin"
       print(x.strip())
    else:
       print("Wrong passcode")     

 else:
    print("Enter correct Username")