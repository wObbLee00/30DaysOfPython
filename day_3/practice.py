#1
age=int(30)
#2
height=float(5.7)
#3
complex_num=1+7j
#4
base=int(input("Enter base: "))
height_in=int(input("Enter height: "))
area=0.5*base*height_in
print(f"The area of the triangle is {area}")
#5
side_a=int(input("Enter side a: "))
side_b=int(input("Enter side b: "))
side_c=int(input("Enter side c: "))
perimeter=side_a+side_b+side_c
print(f"The perimeter of the triangle is {perimeter}")
#6
length=int(input("Enter Length: "))
width=int(input("Enter Width: "))
area_rectangle=length*width
perimeter_rectangle=2*(length+width)
print(f"The area of the rectangle is {area_rectangle}")
print(f"The perimeter of the rectangle is {perimeter_rectangle}")
#7
radius=int(input("Enter radius: "))
area_circle=3.14*radius*radius
circumference=2*3.14*radius
print(f"The area of the circle is {area_circle}")
print(f"The circumference of the circle is {circumference}")
#8
y=0
m_8=2
x=(2+y)/m_8
print("Slope is ",m_8, ", Y intercept is",y)
print("X intercept is",x)
#9
x1,y1=2,2
x2,y2=6,10
m=(y2-y1)/(x2-x1)
euclidean_distance=((x2-x1)**2+(y2-y1)**2)**0.5
print("The slope is",m)
print("The Euclidean distance is",euclidean_distance)
#10
print("The slope in qs 8 is",m_8,"and in qs 9 is",m)
#11
x=-3
y=x**2+6*x+9
print(y)
#12
word="Python"
word_2="dragon"
print(f"length of python is {len(word)} and length of dragon is {len(word_2)}")
print(len(word)!=len(word_2))
#13
a="on"
print(a in word and a in word_2)
#14
sentence="I hope this course is not full of jargon"
word="jargon"
print(word in sentence)
#15
print(a not in word and a not in word_2)
#16
another_word="python"
convert_float=float(len(another_word))
convert_str=str(convert_float)
print(f"The length of the python is {convert_str}")
#17
a=int(input("Enter a number: "))
if a%2==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")
#18
c=int(2.7)
d=7//3
if c==d:
    print("They are equal")
else:
    print("They are not equal")
#19
e="10"
f=10
if type(e)==type(f):
    print("They are of the same type")
else:
    print("They are of different type")
#20
g=int('9.8')
h=10
if g==h:
    print("They are equal")
else:
    print("They are not equal")
#21
hours=int(input("Enter hours: "))
rate=int(input("Enter rate per hour: "))
print(f"Your weekly earning is {hours*rate}")
#22
num_years=int(input("Enter number of years you have lived: "))
print(f"You have lived for {num_years*365*24*60*60} seconds")
#23
n=1
for i in range(1,6):
    print(i,n,i,i*i,i**3)