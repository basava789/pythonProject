
try:
    a=int(input("entre the value:"))
    b=int(input("enter the value:"))
    print(a/b)

except:
    print("invald")
else:
    print("tyr")
finally:
    print("done")

try:
    a=int(input("entre the value:"))
    b=int(input("enter the value:"))
    print(a/b)

except  ValueError as v:
   print ("invalid")
except ZeroDivisionError as e:
    print(" dont entre  the d in zero" )


try:
    a=int(input("entre the value:"))
    b=int(input("enter the value:"))
    if b!=0:
        print(a/b)
    else:
        raise ZeroDivisionError
finally:
    print("done")