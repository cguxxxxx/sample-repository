# add a new line for git sample
#vowels = {'a','e','e','i','o','u','u'}
vowels = set('aeeiouu')
word = 'hello'
u = vowels.union(set(word))
print(vowels)
print(u)

u_list = sorted(list(u))
print(u_list)

t = ('Python',)
print(type(t))

people = {}

people['Ford'] = {
	'Name': 'Ford Prefect',
	'Gender': 'Male',
	'Occupation': 'Researcher',
	'Home Planet': 'Betelgeu Seven'
}

people['Arthur'] = {
	'Name': 'Arthur Dent',
	'Gender': 'Male',
	'Occupation': 'Sandwich-Maker',
	'Home Planet': 'Earth'
}

people['Tricia'] = {
	'Name': 'Tricia McMillan',
	'Gender': 'Female',
	'Occupation': 'Matematician',
	'Home Planet': 'Earth'
}


people['Marvin'] = {
	'Name': 'Marvin',
	'Gender': 'Unkown',
	'Occupation': 'Paranoid Android',
	'Home Planet': 'Unknown'
}

import pprint
pprint.pprint(people)