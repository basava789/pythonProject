
# a={"name":"basava","age":26,"mobile":7895788,"city":"hyd"}
# print(a["name"])
# a["name"]="basavaraja"
# print(a)
# a["mobile"]=789342083
# a["age"]=27
# print(a)
# print(a["age"])
# a["city"]="hyderabad"
# print(a)
# print(a['city'])
# a.pop("city")
# print(a)

def add1(a,b):
    sum=(a+b)
    print(sum)
a=10
b=34
add1(a,b)
def add2(k):
    sum=0

    for i in k:
        sum=(sum+i)
    print(sum)
add2([a,b])

class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

class ver:

    def __init__(self, clr, na, ms, mil):
        self.clr=clr
        self.na=na
        self.ms=ms
        self.mil=mil
class van(ver):
    pass
class bick(ver):
    pass
suvan=van('White', "volov", 200, 20)
print(suvan.clr, suvan.na, "speed:", suvan.ms, "capcity:", suvan.mil)

bick1=bick('yellow',"aidi Q3",185, 55)
print(bick1.clr, bick1.na, 'Speed:', bick1.ms, 'capacity:', bick1.mil)
