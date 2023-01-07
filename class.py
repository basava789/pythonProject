# class rectangle():
#     def read(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         print(self.l*self.b)
#     def parmeter(self):
#         print(2*(self.l+self.b))
# r=rectangle()
# r.read(10,10)
# r.area()
# r.parmeter()

# class reat:
#      def area(self,l,b):
#          print(l*b)
#      def parameter(self,l,b):
#          print(2*(l*b))
# r=reat()
# r.area(10,10)
# r.parameter(10,10)
#
# class rect:
#     def __init__(self, l, b):
#         self.l = l
#         self.b = b
#     def area(self):
#         print(self.l * self.b)
#     def parimeter(self):
#         print(2 * (self.l + self.b))
# p = rect(5, 10)
# p.area()
# p.parimeter()

# class squre:
#      staticmethod
#      def findsqure(n):
#          print(n+n)
# squre.findsqure(10)
#
#
# class hello:
#     def fir(self):
#         print("self")
#
#     def fir(self):
#         print("self",10)
# r=hello()
# r.fir()
# r.fir()

# class emp:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name
#         print("object")
#     def show(self):
#         print(self.name,self.id)
#     def __del__(self):
#        print("destroyed")
# e1=emp(10,"raju")
# e1.show()
# e3=emp(30,'ravi')
# e3.show()
# e2=emp(20,"basava")
# e2.show()

# class v:
#     id=0
#     name=""
#     def show(self):
#         print("id=",v.id ,"name",self.name)
# a=v()
# a.name=""
# a.show()
# v.id=20
# v.name="basava"
# print("id=",v.id,"name=",v.name)

# class bank:
#     bal=100
#     def deposite(self,amt):
#         self.bal=self.bal+amt
#         print("current bal is:-", self.bal)
#     def withdrw(self,amt):
#         self.bal=self.bal-amt
#         print('current bal is :-', self.bal)
#     def getbal(self):
#         print("current bal is :-", self.bal)
#
# bank = bank()
# while True:
#     ch = int(input("enter the ur ch 1.deposite 2.withdrw 3.bal 4.ext"))
#
#     if ch == 1:
#         amt=int(input("enter the amount to deposite "))
#         bank.deposite(amt)
#     elif ch == 2:
#         amt=int(input("entre the amount to withdrw "))
#         bank.withdrw(amt)
#     elif ch == 3:
#         bank.getbal()
#     elif ch == 4:
#         break
#     else:
 #       print("invalid")

class addition:
    def __init__(self):
        self.a=0
        self.b=0
    def readvel(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def __del__(self):
        print("dest called")
c=addition()
print(c.add())
c.readvel(10,20)
print(c.add())
c.readvel(20,100)
print(c.add())
print(c.add())

import  json
b='{"name":"basava","age":27,"lname":"raju"}'

x=json.loads(b)
print(type(x))
print(x)
for a in x:
    print(a,x[a])