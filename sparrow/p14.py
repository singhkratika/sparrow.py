#temperature converter
print("enter for c to f")
print("enter 2 for f to c")
ch=int(input())
if ch==1:
   c=float(input("enter temperature in c:"))
   f=(9*c)/5+32
   print("temperature in f=",f)
elif ch==2:
   f=float(input("enter the temperature in f:"))
   c=(f-32)*5/9
   print("temperature in c= ",c)
 