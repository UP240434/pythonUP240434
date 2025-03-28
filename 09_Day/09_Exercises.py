
# Ejercicios: Nivel 1


#Get user input using input(“Enter your age: ”). 
#If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
print("           ")
print('Programa 1')
age= float(input("Ingresa tu edad:"))
age2 = 18 - age
if age >= 18:
    print('You are old enough to learn to drive')
else:
    print('You need ,',age2 ,', more years to learn to drive.')

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
#You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
print("           ")
print('Programa 2')
Myage= float(input("Mi edad (1):"))
print("           ")
your_age = float(input("Tu edad (2):"))
dif = Myage - your_age
dif2 = your_age - Myage

if dif == 1 or dif2 == 1:
    if dif == 1 or dif2 == 1:
        print('La diferencia es de 1 año')
    else:
        print('')
elif Myage == your_age:
    print('La edad es igual')
else:
    if Myage < your_age:
        print('Tu edad es mayor por:', dif2 , 'años.')
    else:
        print('Mi edad es mayor por:', dif , ' años')

        
#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
print("           ")
print('Programa 3')

num1 = float(input("Ingresa el primer numero (a):"))
num2 = float(input("Ingresa el segundo numero (b):"))

if num1 > num2:
    if num1 > num2:
        print('a es mayor que b')
    else:
        print('a es menor que b')
elif num1 == num2:
         print('a y b son iguales')
elif num1 < num2:
    print ('a es menor que b')

    



# Ejercicios: Nivel 2


#Write a code which gives grade to students according to theirs scores:
print("           ")
print('Programa 2.1')
Cal = float(input("Ingresa la calificacion:"))
if Cal >= 90 and Cal <=100:
    if Cal >= 90 and Cal <=100:
        print('Tu nota es: A')
elif Cal >= 70 and Cal <=89:
         print('Tu nota es: B')
elif Cal >= 60 and Cal <=69:
    print ('Tu nota es: C')
elif Cal >= 50 and Cal <=59:
    print ('Tu nota es: D')
elif Cal >= 0 and Cal <=49:
    print ('Tu nota es: F ')



#Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May,
# the season is Spring June, July or August, the season is Summer
print("           ")
print('Programa 2.2')
Estacion = str(input("Ingresa el mes:"))
Estacion2 = (Estacion.title()) 
if Estacion2 == "Septiembre" or Estacion2 == " Octubre" or Estacion2 == "Noviembre":
    if Estacion2== "Septiembre" or Estacion2 == " Octubre" or Estacion2 == "Noviembre":
        print('La estacion es Otoño')
elif Estacion2 == "Diciembre" or Estacion2 == " Enero" or Estacion2 == "Febrero":
         print('La estacion es Invierno')
elif Estacion2 == "Marzo" or Estacion2 == "Abril" or Estacion2 == "Mayo":
         print('La estacion es Primavera')
elif Estacion2 == "Junio" or Estacion2 == "Julio" or Estacion2 == "Agosto":
         print('La estacion es Verano')


#The following list contains some fruits:
print("           ")
print('Programa 2.3')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = str(input("Ingresa la fruta:")) 
does_exist = fruta in fruits 
print(does_exist)
frutaf = fruits.append(fruta)
if does_exist == True:
    if does_exist == True:
        print('Ya esta la fruta en la lista')
elif does_exist == False:
     print(fruits)




# Ejercicios: Nivel 3

#Here we have a person dictionary. Feel free to modify it!

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

#* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') -
#  for more accurate results more conditions can be nested!

#* If the person is married and if he lives in Finland, print the information in the following format:
print("           ")
print('Programa 3.1')
print("           ")
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