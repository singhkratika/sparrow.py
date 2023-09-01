#LIST
mylist=[]
print("enter ten nos to the list")
for i in range(0,10):
 n=int(input())
 mylist.append(n)
print(mylist)
print("Maximam no= :",max(mylist))
print("Minimum no= :",min(mylist))