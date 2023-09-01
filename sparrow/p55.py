#constructor demo
class rectangle:
 def __init__(self,l,b):
   self.l=l
   self.b=b
 def rectarea(self):
   return(self.l*self.b)
 def rectPeri(self):
   return 2*(self.l+self.b)
x=int(input("enter the length: "))
y=int(input("enter the breadth: "))
r=rectangle(x,y)
print("area of reactangle:",r.rectarea())
print("area of perimeter:",r.rectPeri())
 