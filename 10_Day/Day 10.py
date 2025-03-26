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

first= (person['first_name'])
last = (person['last_name'])
c = (person['country'])
comprobacion = ('skills' in person)
if comprobacion== True:
     print(person['skills'][2])
if 'Python' in person['skills']:
     print ('yes ', 'Python')
if 'JavaScript' and 'React' in person['skills']:
     print ('He is a front end developer')
if 'Node' and 'Python' and "MongoDB" in person['skills']:
     print('He is a backend developer')
if 'React' and  'Node' and 'MongoDB' in person['skills']:
     print('He is a fullstack developer')
else:
     print('unknown title') 
if person['is_marred'] == True and person['country'] == 'Finland':
     print(first, last, 'lives in' , c , 'He is married')