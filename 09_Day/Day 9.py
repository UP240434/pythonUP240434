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

        
Obtener dos números del usuario mediante la solicitud de entrada. Si a es mayor que b, devuelve a mayor que b; si a es menor que b, devuelve a menor que b; de lo contrario,
a es igual a b. Salida:

Enter number one: 4
Enter number two: 3
4 is greater than 3

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
print("           ")
print('Programa 3')
num1 = float(input("Ingresa el primer numero:"))
num2 = float(input("Ingresa el segundo numero:"))
if num1 > num2:
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

# Ejercicios: Nivel 2

#Write a code which gives grade to students according to theirs scores:
print("           ")
print('Programa 2.1')

#Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May,
# the season is Spring June, July or August, the season is Summer
print("           ")
print('Programa 2.2')

#The following list contains some fruits:
print("           ")
print('Programa 2.3')

# Ejercicios: Nivel 3

#Here we have a person dictionary. Feel free to modify it!

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

#* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') -
#  for more accurate results more conditions can be nested!

#* If the person is married and if he lives in Finland, print the information in the following format:
print("           ")
print('Programa 3')
