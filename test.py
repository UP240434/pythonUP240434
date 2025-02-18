

#Program 4
#Wrote a script that pro,pts the user to emter base amd height
#Of the triangle and calculate an area of this triamgle.
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