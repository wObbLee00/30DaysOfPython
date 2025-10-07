#1
list=['Thirty','Days','Of','Python']
joined=" ".join(list)
print(joined)
#2
list2=['Coding','For','All']
joined2=" ".join(list2)
print(joined2)
#3
company="Coding For All"
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[1:])
#10
Company="Coding"
print(company.index(Company))
#11
company=company.replace("Coding","Python")
print(company)
#12
print(company.replace("All","Everyone"))
#13
print(company.split(" "))
#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))
#15
print(company[0])
#16
print(company[-1])
#17
print(company[10])
#18
phrase = "Python For Everyone"
words = phrase.split()
acronym = ''.join(word[0].upper() for word in words)
print(acronym)
#19
phrase = "Coding For All"
words = phrase.split()
acronym = ''.join(word[0].upper() for word in words)
print(acronym) 
#20
company="Coding For All"
print(company.index("C"))
#21
print(company.index("F"))
#22
print(company.rfind("l"))
#23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
#24
print(sentence.rindex("because"))
#25
print(sentence.replace('because', ''))
#26
company="Coding For All"
print(company.startswith("Coding"))
#27
print(company.startswith("coding"))
#28
string='   Coding For All      '
print(string.strip())
#29
var1='30DaysOfPython'
var2='thirty_days_of_python'
print(var1.isidentifier())
print(var2.isidentifier())
#30
list=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list))
#31
print("I am enjoying this challenge.\nI just wonder what is next.")
#32
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
#33
radius=10
area=3.14*radius**2
print("The area of a circle with radius {} is {} meters square.".format(radius,area))
#34
a=8
b=6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")
