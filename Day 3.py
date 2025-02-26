#Program 1
#Declare your age as integer variable
Edad = int(input("Ingresa tu edad: "))
print ("Tu edad es:", " ",Edad) 
print(type(int(Edad)))

#Program 2
#Declare your height as a float variable
Edad = float(input("Ingresa tu edad: "))
print ("Tu edad es:", " ",Edad) 
print(type(float(Edad)))

#Program 3
#Declare a variable that store a complex number
complex = float(input("Ingresa tu numero: "))
print('Complex number: ', 1 + 1j)

#Program 4
#Wrote a script that prompts the user to enter base and height
#Of the triangle and calculate an area of this triangle.
# (area = 0.5 x b x h)
base = float (input("Ingresa el valor de la base: "))
altura = float (input ("Ingresa el valor de la altura: "))
area = (base*altura*0.5)
print ("El area del triangulo es", " ",area) 

#Program 5
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#Calculate the perimeter of the triangle 
#(perimeter = a + b + c).
a = float(input("Ingresa el valor del lado a: "))
b = float(input("Ingresa el valor del lado b: "))
c = float(input("Ingresa el valor del lado c: "))
perimeter = (a+b+c)
print("El perimetro del triangulo es:", " ",perimeter)

#Program 6
#Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) 
# and perimeter (perimeter = 2 x (length + width))
lenght = float(input("Ingresa el largo del rectangulo: "))
width = float(input("Ingresa el ancho del rectangulo: "))
area = (lenght * width)
perimeter = (lenght + width)
print("El area del rectangulo es:"," ",area)
print("El perimetro del rectangulo es:"," ",perimeter)

#Program 7
#Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) 
# and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = float(input("Ingresa el valor del radio: "))
area = pi * r * r 
c = 2 * pi * r 
print("El area del circulo es:"," ",area)
print("La circunferencia del circulo es:"," ",c)

#Program 8
# Calculate the slope, 
# x-intercept 
# and y-intercept of y = 2x -2
x= float(input("Ingresa el valor de x: "))
y = 2 * x - 2
print("El valor de y es:"," ",y)

#Program 9
# Slope is (m = y2-y1/x2-x1).
# Find the slope and Euclidean distance between point (2, 2) 
# and point (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
m = (y2 - y1)/(x2-x1)
print("El valor de m es:"," ",m)

#Program 10
#Compare the slopes in tasks 8 and 9.





#Program 11
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x= float(input("Ingresa el valor de x: "))
y =( (x**2)+(6*x)+9)
print ("El valor de y es:", " ",y) 
if y == 0:
    print("y es igual 0.")
else:
    print("y no es igual a 0.")

#Program 12
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
pyhton = ("python")
dragon = ("dragon")
print (len (pyhton))
print (len (dragon))
print(len('python') > len('dragon'))   # False

#Program 13
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
pyhton = ("python")
dragon = ("dragon")
print ("on in python and dragon", "on" in "python and dragon"," ")

#Program 14
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print ("jargon in I hope this course us not full of jargon", "jargon" in "I hope this course us not full of jargon"," ")

#Program 15
#There is no 'on' in both dragon and python
print ("On in python ", "On" in "python "," ")
print ("On in dragon ", "On" in "dragon"," ")

#Program 16
#Find the length of the text python and convert the value to float 
# and convert it to string
pyhton = ("python")
longTexto = len(pyhton)
print (longTexto)
floatLong = float (longTexto)
strlong = str (floatLong)
print (type(strlong))

#Program 17
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

#Program 18
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

#Program 19
#Check if type of '10' is equal to type of 10

#Program 20
#Check if int('9.8') is equal to 10

#Program 21
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?