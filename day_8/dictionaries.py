#excercise 1
#q1
dog={}
#q2
dog['name']='ismail'
dog['color']='sanwala'
dog['breed']='monkey'
dog['legs']=4
dog['age']=17
#q3
student_dic={'first_name':'wabil','last_name':'butt','gender':'male','age':22,'marital_status':'married','skills':['brave','bold'],'country':'pakistan','city':'sialkot','address':'azeem colony'}
#q4
print(len(student_dic))
#q5
print(student_dic.get('skills'))
print(type(student_dic.get('skills')))
#q6
student_dic['skills'].append('beautiful')
print(student_dic.get('skills'))
#q7
dic_keys=student_dic.keys()
print(dic_keys)
#q8
dic_values=student_dic.values()
print(dic_values)
#q9
print(student_dic.items())
#q10
del student_dic['skills']
print(student_dic)
#q11
del student_dic
print(student_dic)