#Level 1
import sys
print(sys.version)
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(3%4)
print(3//4)
print(3**4)

name="Wabil"
familyname="Nadeem Butt"
Country="Pakistan"
feeling="I am enjoying 30 days of python"

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh','Python','Finland']))
print(type(name))
print(type(familyname))
print(type(Country))

#Level 2
print(type(-1))
print(type(7.88))
print(type(1+9j))
print(type("wObbLee"))
print(type(False))
print(type(["Pakistan","India"]))
print(type(("Ahmed","Babar")))
print(type({"Shah",6.7}))
print(type({'name':['Goland','Mistake','Sathi'], 'area':'Hell', 'Age':99}))

a=(2,3)
b=(10,8)
def euclidian_distance(a,b):
    distance=((b[0]-a[0])**2+(b[1]-a[1])**2)**0.5
    return distance
print(euclidian_distance(a,b))