#excercise 1
#q1
age=int(input("Enter your age: "))
if age>= 18:
    print("You are old enough to learn to drive.")
else:
    years_left=18-age
    print(f"You need {years_left} more years to learn to drive.")
#q2
my_age=22
your_age=int(input("Enter your age: "))
if my_age>your_age:
    diff=my_age-your_age
    print(f"You are {diff} years younger than me")
elif my_age==your_age:
    print("You are the same age as me")
else:
    diff=your_age-my_age
    print(f"You are {diff} years older than me")
#q3
a=int(input("Enter number one: "))
b=int(input("Enter number two: "))
if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} and {b} are equal")

#excercise 2
#q1
score=75
if score>=80 and score<=100:
    print("Grade: A")
elif score>=70 and score<=79:
    print("Grade: B")
elif score>=60 and score<=69:
    print("Grade: C")
elif score>=50 and score<=59:
    print("Grade: D")
else:
    print("Grade: F")
#q2
month=input("Enter month: ")
if month=="December" or month=="January" or month=="February":
    print("Season is Winter")
elif month=="March" or month=="April" or month=="May":
    print("Season is Spring")
elif month=="June" or month=="July" or month=="August":
    print("Season is Summer")
else:
    print("Season is Autumn")
#q3
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit=input("Enter Fruit: ")
if user_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(user_fruit)
    print(fruits)

#excercise 3

#q1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    mid=int(len(person['skills'])/2)
    print(person["skills"][mid])
    if 'Python' in person['skills']:
        print("Python is in skills.")
    else:
        print("Python not in skills")
    if 'Javascript' in person['skills'] and 'React' in person['skills']:
        print("He is a front end developer")
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB'in person['skills']:
        print("He is a backend developer")
    elif 'Node' in person['skills'] and 'React' in person['skills'] and 'MongoDB'in person['skills']:
        print("He is a full stack developer")
    else:
        print("Unknown title")
if person['is_marred']==True:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
