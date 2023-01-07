#b=1001
#c=[]
#for i in range(100,1001):
    #if i%7==0:
       # c.append(i)
#print(c)


ste = int(input("enter the ste num:-"))
end = int(input("enter the end num:-"))
n = int(input("enter the division num:-"))
a=[]
for i in range(ste,end):
    if i%n == 0:
      a.append(i)
print(a)