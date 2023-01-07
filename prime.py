a = int(input("enter the num:-"))
b = []
d = []
for n in range(a+1):
    c = 0
    for i in range(2,n):
        if n%i == 0:
            c=c+1
    if c == 0:
         b.append(n)
    else:
        d.append(n)
print(b)
print(d)

