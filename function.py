
# a=30
# def hello():
#     a=10
#     print(a)
# hello()
# print(a)
#
# a=30
# def hello():
#     global a
#     a=10
#     print(a)
# hello()
# print(a)



# def add(a,b):
#     c=(a+b)
#     print("sum",c)
# def diff(a,b):
#     c=(a-b)
#     print("diff", c)
# def multipy(a,b):
#     c=(a,b)
#     print("multipy",c)
# a=int(input("enter the value :"))
# b=int(input("enter the value"))
#
# while True:
#     ch=int(input("select ur chioce \n 1. add 2.diff 3.multipy 4.exit"))
#     if ch==1:
#         add(a,b)
#     elif ch==2:
#         diff(a,b)
#     elif ch==3:
#         multipy(a,b)
#     else:
#         break

# def add(a,b):
#     c=(a+b)
#     print("sum",c)
# def diff(a,b):
#     c=(a-b)
#     print("diff",c)
# def multipy(a,b):
#     c=(a*b)
# def divison(a,b):
#     c=(a/b)
# a=int(input("enter the value"))
# b=int(input("enter the value"))
#
# while True:
#     ch=int(input("enter ur choice \n 1.add 2.diff 3.multipy 4.divison 5.exit"))
#     if ch == 1:
#         print(a+b)
#     elif ch == 2:
#         print(a-b)
#     elif ch == 3:
#         print(a*b)
#     elif ch == 4:
#         print(a/b)
#     else:
#         break
a=18
def hello():
    global a
    a=10
    print(a)
print(a)
hello()
print(a)

x=4
def te():
    global x
    x=45
    print(x)
print(x)
te()
print(x)
te()