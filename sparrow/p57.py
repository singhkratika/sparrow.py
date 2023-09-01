#MULTILEVEL
class A():
 def m1(self):
  print("hello this is m1 from A")
class B(A):
 def m2(self):
  print("hello this is m2 from B")
class C(B):
 def m3(self):
  print("this is m3 from C")
c=C()
c.m1()
c.m2()
c.m3()