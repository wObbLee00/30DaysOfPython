#excercise 1

#q1
empty_list=[]
#q2
list_with_5_items=['Potato','Hat','Dog','Cat','Iron']
#q3
print(len(list_with_5_items))
#q4
mid=int(len(list_with_5_items)/2)
print(f"First Item: {list_with_5_items[0]}")
print(f"Middle Item: {list_with_5_items[mid]}")
print(f"Last Item: {list_with_5_items[-1]}")
#q5
mixed_data_types=['wabil','22','5 foot 7 inches','Committed','Pakistan']
#q6
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
#q7
print(it_companies)
#q8
print(len(it_companies))
#q9
mid=int(len(it_companies)/2)
print(f"First Company: {it_companies[0]}")
print(f"Middle Company: {it_companies[mid]}")
print(f"Last Company: {it_companies[-1]}")
#q10
it_companies[0]='Brackets'
print(it_companies)
#q11
it_companies.append('Facebook')
#q12
mid=int(len(it_companies)/2)
it_companies.insert(mid,'Devsinc')
#q13
mid=int(len(it_companies)/2)
print(it_companies[mid].upper())
#q14
string_char='#'
it_companies.extend(string_char)
#q15
existence='Apple' in it_companies
print(existence)
#q16
it_companies.sort()
print(it_companies)
#q17
it_companies.sort(reverse=True)
print(it_companies)
#q18
del it_companies[0:2]
print(it_companies)
#q19
del it_companies[-3:]
print(it_companies)
#q20
mid=int(len(it_companies)/2)
del it_companies[mid]
print(it_companies)
#q21
del it_companies[0]
print(it_companies)
#q22
del it_companies[-1]
print(it_companies)
#q24
it_companies.clear()
print(it_companies)
#q26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
full_stack=front_end.copy()
index_after_redux=full_stack.index('Redux')+1
full_stack.insert(index_after_redux,'Python')
full_stack.insert(index_after_redux,'SQL')
print(full_stack)

#excercise 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
maximum=max(ages)
minimum=min(ages)
print(maximum,minimum)
#2
ages.append(maximum)
ages.append(minimum)
#3
median_age=int(len(ages)/2)
#4
average_age=sum(ages)/2
#5
range_of_ages=maximum-minimum
#6
min_average=abs(minimum-average_age)
max_average=abs(maximum-average_age)
#7
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
mid=int(len(countries)/2)
print(countries[mid])

#8
First_half=countries[0:mid]
Second_half=countries[mid:]
print(First_half)
print(Second_half)

#9
Countries_2=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first,second,third,*scandic=Countries_2