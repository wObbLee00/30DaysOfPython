#excercise 1

#q1
empty_tuple=()
#q2
siblings=('ismail','nawal')
#q3
brothers=('ismail')
sisters=('Nawal')
siblings=brothers+sisters
#q4
print(len(siblings))
#q5
father=('nadeem')
mother=('asma')
family_members=siblings+father+mother

#excercise 2

#q1
sibling_1,sibling_2,*parents=family_members
#q2
fruits=('mango','banana')
vegetables=('Lady Finger','Potato')
animal_products=('Chicken','beef')
food_stuff_tp=fruits+vegetables+animal_products
#q3
food_stuff_lt=list(food_stuff_tp)
#q4
mid=int(len(food_stuff_tp)/2)
print(food_stuff_tp[mid])
mid=int(len(food_stuff_lt)/2)
print(food_stuff_lt[mid])
#q5
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])
#q6
del food_stuff_tp
#q7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)
