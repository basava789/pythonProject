# import math
# n=math.pow(10,2)
# print("the power of num:-",n)
# n=math.ceil(10.34413)
# print("the ceil value:- ",n)
# n=math.floor(10.5653)
# print("floor value :-",n)
# n=math.fabs(-10)
# print("abs the value:-",n)
# n=math.factorial(5)
# print("the factorial value:-",n)
# m=round(5.7887)
# print(m)
import time
# import random
# print('the from the list:-',end='')
# print(random.choice([40,28,27,282,22]))
# print("the random form the list:-",end="")
# print(random.choice(range(1,500)))
# print("a random num from ranrang:-",end='')
# print(random.randrange(100,500,30))
# print("the random num to be 0 and 1:",end="")
# print(random.random())
from datetime import date
from datetime import datetime
today=date.today()
print(today)
print(datetime.now())
time.sleep(3)
print(datetime.time(datetime.now()))

print(datetime.now().strftime("%d"))
print(datetime.now().strftime("%B"))
print(datetime.now().strftime("%y"))
from datetime import timedelta
begidatestring= date.today()
print(begidatestring)
enddate=begidatestring+timedelta(days=4)
print(enddate)
print("diff=",(enddate-begidatestring).days)

print("hello",end="")
print('world')