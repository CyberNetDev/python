file = open("fil.txt","a")
newItem=[]
while newItem!="exit":
    newItem=input("enter:")
    file.write(newItem+"\n")
else:
     print("ok")
file.close