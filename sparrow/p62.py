name=input("enter name")
shortname=name.split(" ")
#print(shortname)
print("your short name:",end="")
for n in range(len(shortname)-1):
 print(shortname[n][0]+".",end="")
print(shortname[len(shortname)-1])
