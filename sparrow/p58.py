#MULTIPLE
class papa:
 def m1(self):
  print("mai m1 papa se hu")
class mummy:
 def m2(self):
  print("mai m2 mummy se hu")
class child(mummy,papa):
 def m3(self):
  print("mai m3 hu papa and mummy ka baccha hu")
c=child()
c.m3()
c.m2()
c.m1()