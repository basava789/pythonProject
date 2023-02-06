# import sys
# print("Python version")
# print(sys.version)
import collections

# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)


# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))

# culure=['red', 'yellow', 'you', 'know']
# print(culure[0], culure[3])

# exam = (11, 12, 2014)
# print("The examination will start from : %i / %i/ %i" %exam)
#
# a=int(input("value = "))
# n1=a
# n2=int("%s%s" % (a, a))
# n3=int('%s%s%s' %(a, a, a))
# print(n1+n2+n3)
#
# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))
#
# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days


# def test(nums):
#     return nums.count(19) == 2 and nums.count(5) >= 3
# nums = [19,19,15,5,3,5,5,2]
# print("Original list:")
# print(nums)
# print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
# print(test(nums))
# nums = [19,15,15,5,3,3,5,2]
# print("\nOriginal list:")
# print(nums)
# print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
# print(test(nums))
# nums = [19,19,5,5,5,5,5]
# print("\nOriginal list:")
# print(nums)
# print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
# print(test(nums))

#
# def binarysearch(arr, n, k):
#
#     a = 0
#     b = n - 1
#     while k in arr:
#         x = (a + b) // 2
#         if arr[x] < k:
#             a = x + 1
#         elif arr[x] > k:
#             b = x - 1
#         else:
#             return x
#     return -1
# print(binarysearch(arr=[1, 2, 3, 4, 5], n=5, k=4))

# def reverse_groups(arr, n, k):
#     for i in range(0, n, k):
#         left = i
#         right = min(i + k - 1, n - 1)
#         while left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
#     return arr
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# n = len(arr)
# k = 7
# print(reverse_groups(arr, n, k))

# a=[19,45,87,67,43,90,43]
# b=[]
# for i in a:
#     if i <=50:
#         b.append(i)
# print(b)

# v=[12, 23, 23, 45, 12, 17, 8, 17, 8, 9]
# dup=[]
# for v,count in collections.Counter(v).items():
#     if count >1:
#         dup.append(v)
# print(dup)

# import calendar
# y=int(input("enter the year ="))
# m=int(input("entre the month ="))
# print(calendar.month(y, m))

# n=int(input("enrte num="))
# if n <=17:
#     print(17-n)
# else:
#     print((n-17)*2)

# a=int(input("entre num ="))
# b=int(input("entre num ="))
# c=int(input("entre num ="))
# if a==b and b==c and c==a:
#     print((a+b+c)*3)
# else:
#     print(a+b+c)
#

#
# a="arry"
# # print("is " +a)
# # print(a)
# add="is"
# add+=a
# print(" " +add)

# n=int(input('entre the num ='))
# if n%2==0:
#     print('ITS Even number')
# else:
#     print("odd number")

#
# a=[2, 2, 4, 5, 7, 5, 5, 9]
# if len(a)==8 and a.count(a[3])==3:
#     print(a)
# else:
#     print("not valid")

import pytest
# def check_list(lst):
#     if len(lst) == 6 and lst.count(lst[4]) >= 2:
#         return True
#     return False
# lst = [1, 2, 3, 4, 5, 5]
# print(check_list(lst))
#
# lst= [2, 3, 4, 6, 5, 7]
# print(check_list(lst))

# lst= [4, 5, 6, 7, 8, 8]
# print(check_list(lst))

def list(n):
    if n% 34 ==4 and n>= 4**4:
        return True
    return False
n=912
print(list(n))

n=922
print(list(n))

n=854
print(list(n))

n=788
print(list(n))

def soultion(digits: str,num: str) -> int:
    # write code
    return 0
# giv