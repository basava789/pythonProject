# def add1(a,b):
#      sum=(a+b)
#      print(sum)
#
# def add2(va):
#     sum=0
#     for x in va:
#          sum=sum+x
#     print(sum)
# a=10
# b=19
# add1(a, b)
# add2([a,b])


# def add1(a,b,c=50):
#          sum=(a+b+c)
#
#          print(sum)
#
# a=10
# b=20
# c=40
# add1(a,b,c)
# add1(a,b)
#
# def s(name,age):
#     print("std det:-",name,age)
# s("basava",20)
# s(name="basava",age=20)
# s("basava",age=20)
#
# def par(*kvr):
#     sum=0
#     for i in kvr:
#         sum=sum+1
#     avg=sum/len(kvr)
#     print("avrg:-",avg)
# par(67,78,90)
#
#
# def per(**l):
#     sum=0
#     for sub in l:
#         sub_name=sub
#         sub_marks=l[sub]
#     print(sub_name,":",sub_marks)
#per(mat=70,eng=56,sce=75)
# class raaj():
#     def ra(self,n):
#         for i in range(1, 11):
#             print(i*n)
# ba=raaj()
# ba.ra(9)

import pytest
import requests
import json
def test_yy():
    url="https://gorest.co.in/public/v2/users"
    reep=requests.get(url)
    j=json.loads(reep.text)
    assert reep.status_code==200, 'Responce code should be 200 but came '+str(reep.status_code)
    assert j[0]['id']==3999,reep.text
    assert j[0]['name']=='Rajinder Gill', reep.text
    assert j[0]['email']=='gill_rajinder@koss.info',reep.text
    assert j[0]['gender']=='female',reep.text
    assert j[0]['status']=='active',reep.text

