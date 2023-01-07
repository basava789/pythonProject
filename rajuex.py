# #1
# a=[12,23,45,56]
# b=sum(a)
# print(b)
# #2
# import math
# c=[23,3, 2, 2, 3, 3]
# v=math.prod(c)
# print(v)#("63888")
# #3
# from operator import *
# list=[22,22,33,2]
# m=1
# for i in list:
#     m=mul(i,m)
# print(m)
# #4
# x=[21,22,34,56]
# print(max(x))
# print(min(x))
#
# #5
# def match_words(words):
#   ctr = 0
#
#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#       ctr += 1
#   return ctr
#
# print(match_words(['abc', 'xyz', 'aba', '1221']))
#
#
# def addation(n):
#     if n:
#         return n+addation(n-1)
#     else:
#         return n
# res=addation(10)
# print(res)

from selenium import webdriver
from webdriver_manager import chrome
import pytest
import time

def test_ravi():
    drive=webdriver.Chrome()
    drive.get("https://www.google.com/")
    drive.maximize_window()
    drive.get_window_size()
    print(drive.title)
    time.sleep(5)
    drive.get("https://www.youtube.com/")
    drive.maximize_window()
    time.sleep(3)
    drive.close()

from selenium import webdriver
from webdriver_manager import chrome
import time
import pytest

def test_uk():
    driv=webdriver.Chrome()
    driv.get('https://www.youtube.com/')
    driv.maximize_window()
    print(driv.title)
    time.sleep(6)
    driv.close()