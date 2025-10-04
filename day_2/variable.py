#Day 2: 30 Days of python programming
#Level 1
first_name="Wabil"
last_name="Nadeem Butt"
full_name="Wabil Nadeem Butt"
country="Pakistan"
city="Sialkot"
age=22
year=2025
is_married=False
is_true=True
is_light_on=False
a,b,c,d=1,2,3,4

#Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(f"Length of full name is {len(first_name)} and length of last name is {len(last_name)}")
num_one,num_two=5,4
total=num_one+num_two
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_two%num_one
floor_division=num_one//num_two
print(f"Total: {total}, Diff: {diff}, Product: {product}, Division: {division}, Remainder: {remainder}, Floor Division: {floor_division}")
radius=int(30)
area_of_circle=3.14*(radius**2)
circum_of_circle=2*3.14*radius
print(f"Area of circle: {area_of_circle}, Circumference of circle: {circum_of_circle}")
radius=int(input("Enter radius: "))
area_of_circle=3.14*(radius**2)
print(f"Area of circle: {area_of_circle}")

first_name=input("Enter first name: ")
last_name=input("Enter last name: ")
country=input("Enter country: ")
age=input("Enter age: ")
print(f"Your name is {first_name} {last_name}. You are {age} years old and you live in {country}.")
help('keywords')