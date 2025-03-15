# EXERCISES: LEVEL 1.

#Find the length of the set it_companies
print("           ")
print('Programa 1')
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))


#Add 'Twitter' to it_companies
print("           ")
print('Programa 2')
it_companies.add('Twitter')
print (it_companies)


#Insert multiple IT companies at once to the set it_companies
print("           ")
print('Programa 3')
other_ti = {'Instagram', 'Youtube', 'WhatsApp'}
print(it_companies.union(other_ti))


#Remove one of the companies from the set it_companies
print("           ")
print('Programa 4')
it_companies.remove('IBM')
print(it_companies)


#What is the difference between remove and discard
print("           ")
print('Programa 5')
print('Eliminar es borrar todo dato de la base de datos y decartar es algo que no tiene valor')
print("           ")


# EXERCISES: LEVEL 2.


#Join A and B
print("           ")
print('Programa 2.1')
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
print(a.union(b))

#Find A intersection B
print("           ")
print('Programa 2.2')
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
print(a.intersection(b) )

#Is A subset of B
print("           ")
print('Programa 2.3')
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
print(a.issubset(b))

#Are A and B disjoint sets
print("           ")
print('Programa 2.4')
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
print(a.isdisjoint(b))

#Join A with B and B with A
print("           ")
print('Programa 2.5')
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
print(a.union(b))
print("           ")
print(b.union(a))

#What is the symmetric difference between A and B
print("           ")
print('Programa 2.6')
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
print(a.symmetric_difference(b))


#Delete the sets completely
print("           ")
print('Programa 2.7')
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
del a
del b



# EXERCISES: LEVEL 3.


#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print("           ")
print('Programa 3.1')
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(age)
lenAge = len(age)
print(len(age))
print("           ")
age2 = set(age)
print(age2)
lenAge2 = len(age2)
print(len(age2))
print("           ")
if (lenAge>lenAge2):
    print ('La lista es mayor')
else:
    print("El set es mayor")


#Explain the difference between the following data types: string, list, tuple and set
print("           ")
print('Programa 3.2')
print('Cualquier tipo de datos escrito como texto es una cadena. Cualquier dato entre comillas simples, dobles o triples es una cadena.')
print("           ")
print('Una lista es una colección de distintos tipos de datos que está ordenada y es modificable '
'. Una lista puede estar vacía o puede tener elementos de distintos tipos de datos. Ademas se anota entre corchetes [], comillas y comas')
print("           ")
print("Una tupla es una colección de diferentes tipos de datos que está ordenada y no se puede cambiar (inmutable). Las tuplas se escriben entre corchetes, (), comillas y comas.")
print("           ")
print('Un conjunto es una colección de elementos distintos no ordenados y no indexados.'
' En Python, un conjunto se usa para almacenar elementos únicos y es posible encontrar la unión. Se anota entre llaves {}, comillas y comas.')
print("           ")

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
print("           ")
print('Programa 3.3')
list = ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and' ,'teach', 'people']
print(list)
lenlist = len(list)
print(len(list))
print("           ")
set = set(list)
print(set)
print(len(set))


