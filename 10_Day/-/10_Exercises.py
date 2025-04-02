
#Exercises: Level 1


#Iterate 0 to 10 using for loop, do the same using while loop.
print("           ")
print('Programa 1')
count = 0
while count < 10:
    print(count)
    count = count + 1
else:
    print(count)

print("           ")
numeros = (0, 1, 2, 3, 4, 5,6,7,8,9, 10)
for numero in numeros:
    print(numero)

#Iterate 10 to 0 using for loop, do the same using while loop.
print("           ")
print('Programa 2')
count = 10
while count > 0:
    print(count)
    count = count - 1
else:
    print(count)
    
print("           ")
numeros = (10, 9, 8, 7, 6, 5,4,3,2,1,0)
for numero in numeros:
    print(numero)

#Write a loop that 
print("           ")
print('Programa 3')
for i in range (0,8):
    print('#' * i)    


#Use nested loops to create the following:
print("           ")
print('Programa 4')
lado = 8
for i in range(lado):
    for j in range(lado):
        print("# ", end="")
    print()

#Print the following pattern:
print("           ")
print('Programa 5')
for n in [0,1,2,3,4,5,6,7,8,9,10]:
  cuadrado = n**2
  print(n, '*', n ,'=' ,cuadrado)


#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("           ")
print('Programa 6')
programs = ['Python', 'Numpy','Pandas','Django', 'Flask']
for program in programs: # number is temporary name to refer to the list's items, valid only inside this loop
    print(program)

#Use for loop to iterate from 0 to 100 and print only even numbers
print("           ")
print('Programa 7')
for numero in range(0,100,2):
    print(numero)
else:
    print(numero + 2)

#Use for loop to iterate from 0 to 100 and print only odd numbers
print("           ")
print('Programa 8')
for numero in range(1,100,2):
    print(numero)



#Exercises: Level 2

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
print("           ")
print('Programa 2.1')
suma = 0
for n in range(0,101):
  suma = suma + n
print('La suma es:', suma,)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print("           ")
print('Programa 2.2')
suma = 0
for n in range(0,102,2):
  suma = suma + n
print('La suma par es:', suma)
suma = 0
for n in range(1,100,2):
  suma = suma + n
print('La suma impar es:', suma)





#Exercises: Level 3

#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
print("           ")
print('Programa 3.1')
import paises as p
paisess = p.countries
for pais in paisess:
    if 'land' in pais:
        print(pais)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print("           ")
print('Programa 3.2')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
for fruit in fruits:
    print(fruit)


#Go to the data folder and use the countries_data.py file.

#What are the total number of languages in the data
#Find the ten most spoken languages from the data
#Find the 10 most populated countries in the world
print("           ")
print('Programa 3.3')
import countries_data as cd
countrieslist = cd.countries
list_data = countrieslist
total_languages_initial = []
for i in list_data:
    total_languages_initial.extend(i["languages"])
print("Languages = ", len(set(total_languages_initial)))
counts = {}
for i in total_languages_initial:
    counts[i] = counts.get(i, 0) + 1


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


counts = sort_dict_by_value(counts, True)
for i in list(counts.items())[:10]:
    print(i)
populations = {}
for i in list_data:
    populations[i["name"]] = i["population"]
populations = sort_dict_by_value(populations, True)
for i in list(populations.items())[:10]:
    print(i)