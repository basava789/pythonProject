year = int(input("enter the yera:-"))

if (year%400 == 0) and (year%100 == 0):

         print(year," : leap year")

elif (year%4 == 0) and (year%100 != 0):

        print(year,": leap year")
else:
      print( year,": not a leap year")
