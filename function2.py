
#types of function

import os
print(os.getcwd())
os.rename("cons.py","exp.py")
c=open("exp.py","r")
print(c.read())
c.close()
#
# import datetime
# import time
# def de(a):
#     sum=0
#     for i in a:
#         sum=sum+1
#         return sum
# a=[10,10,20,50,60]
# x=sum(a)
# print(x)
#
# y=(12,12,3,4,4,40)
# print(y)
# print(datetime.datetime.now())
# for x in y:
#     print(x)
#     time.sleep(2)
# print(datetime.datetime.now())

import math
def fact(n):
    if n<0:
        return -1
    elif n == 0:
        return 1
    else:
        f= 1
        for i in range(n, 0, -1):
            f=f*i
            return f

def fect(n):
    if n<0:
        return -1
    elif n== 0:
        return 1
    else:
        return n*fect(n-1)
n=int(input("enter the value :-"))
print(fact(n))
print(fect(n))
print(math.factorial(n))

x=lambda a:a+10
print("sum", x(20))
y=lambda b:b*3
print("sum", y(3))

def getpower(c):
    return lambda power:c*power
power=getpower(10)
print(power)

