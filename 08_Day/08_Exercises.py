
#Create an empty dictionary called dog
print("           ")
print('Programa 1')
dog_dict = {}
print(dog_dict)

#Add name, color, breed, legs, age to the dog dictionary
print("           ")
print('Programa 2')
dog_dict = {
    'info':''
    
}
dog_dict['info'] = ('CHarlotte, Cafe, Chihuahua, Patas Cortas, 9 años')
print(dog_dict)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
print("           ")
print('Programa 3')
student  = {
    'Nombre':'Gae;',
    'Apellido(s)':'Quirarte Sandoval',
    'Genero':'Masculino',
    'Edad':18,
    'Estado Civil':'Soltero',
    'Habilidades':['Agil', 'Atento', 'Responsable',],
    'Pais':'Mexico',
    'Ciudad y Direccion':'',
   
}

student ['Ciudad y Direccion'] = 'Calle Dr Narciso Gonzalez 22 A, Juchipila, Zacatecas.'
print(student)

#Get the length of the student dictionary
print("           ")
print('Programa 4')
print(len(student))

#Get the value of skills and check the data type, it should be a list
print("           ")
print('Programa 5')
Habil= (student.get('Habilidades'))
lista = list(Habil)
print (lista)
print(type(lista))


#Modify the skills values by adding one or two skills
print("           ")
print('Programa 6')
student['Habilidades'].append('Social, Organizado')
print(student)

#Get the dictionary keys as a list
print("           ")
print('Programa 7')
keys = student.keys()
print(keys) 
lista = list(keys)
print (lista)
print(type(lista))

#Get the dictionary values as a list
print("           ")
print('Programa 8')
values = student.values()
print(values)  
lista = list(values)
print (lista)
print(type(lista))

#Change the dictionary to a list of tuples using items() method
print("           ")
print('Programa 9')
tupla = student.items()
print(tupla)
print(type(tupla))

#Delete one of the items in the dictionary
print("           ")
print('Programa 10')
student.popitem() 
print(student)

#Delete one of the dictionaries
print("           ")
print('Programa 11')
del student
