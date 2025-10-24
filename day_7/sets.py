#excercise 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#q1
print(len(it_companies))
#q2
it_companies.add('Twitter')
#q3
it_companies.update(['Devsinc','Disney'])
print(it_companies)
#q4
it_companies.remove('Google')
#q5
#if the word is not in the set, remove returns an error but discard doesnt

#excercise 2

#q1
print(A.union(B))
#q2
print(A.intersection(B))
#q3
print(A.issubset(B))
#q4
print(A.isdisjoint(B))
#q5
print(A.union(B))
print(B.union(A))
#q6
print(A.symmetric_difference(B))
#q7
del A
del B

#excercise 3

#q1
lenght_list=len(age)
length_set=len(set(age))
if lenght_list>length_set:
    print("Length of list is greater")
else:
    print("Length of set is greater")

#q3
sentences="I am a teacher and I love to inspire and teach people"
sentences_set=set(sentences)
print(len(sentences_set))