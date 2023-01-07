# def name(firstname, lastname):
#     print('your name is:-', firstname, lastname)
#
# name("basava",''"raja")
#
def file(a,b):
    a=input( "enter first name :-")
    b=input("enter last name:-")
    print('full name is:-', a, b)

file("a","b")
#
# def well():
#     print("your name is:-", "Basava raja")
# well()

def raju(a,b):
    a=int(input("enter:-"))
    b=int(input("enter:-"))
    f=[]
    d=[]

    for i in range(a,b):
        c = 0
        for n in range(2,i):
            if i%n == 0:
                c = c+1
        if c == 0:
            d.append(i)
        else:
            f.append(i)
    print("prime num:-", d)
    print("not prime num:-",f)
raju("a","b")


def hello(a,b):
    a=int(input("enter the value:-"))
    b=int(input("enter the value:-"))
    x=[]
    y=[]
    for i in range(a,b):
        c=0
        for n in range(2,i):
            if i%n==0:
                c=c+1
        if c==0:
            x.append(i)
        else:
            y.append(i)
    print(x)
    print(y)
hello('a','b')