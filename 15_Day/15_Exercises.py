
#Abra su shell interactivo de Python y pruebe todos los ejemplos cubiertos en esta sección.
print("           ")
print('Programa 1')


#Este es un error de Syntaxis.
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
#print 'hello world'
print('hello world')


#Este es un error de Nombre.
#NameError: name 'age' is not defined
#print(age)
print("           ")
age = 25
print(age)


#Este es un error de Indice
#IndexError: list index out of range
#numbers = [1, 2, 3, 4, 5]
#print(numbers[5])
print("           ")
numbers = [1, 2, 3, 4, 5]
print(numbers[4])


#Este es un eror de ModuleNotFoundError
#import maths
#En el ejemplo anterior, añadí deliberadamente una "s" extra a la función "matemáticas" y se generó un error "MóduloNotFoundError" .
#Para solucionarlo, eliminemos la "s" extra de la función "matemáticas".
print("           ")
import math


#Este es un error de AttributeError
#math.PI
#Como pueden ver, ¡me equivoqué de nuevo! En lugar de pi, intenté llamar a una función PI desde el módulo de matemáticas. 
#Se generó un error de atributo; es decir, la función no existe en el módulo. Vamos a corregirlo cambiando de PI a pi.
print("           ")
print(math.pi)


#Este es un error de  KeyError
#users = {'name':'Asab', 'age':250, 'country':'Finland'}
#print(users['name'])
#print(users['county'])
#Como pueden ver, hubo un error tipográfico en la clave usada para obtener el valor del diccionario. 
#Por lo tanto, se trata de un error de clave y la solución es bastante sencilla. 
print("           ")
users = {'name':'Asab', 'age':250, 'country':'Finland'}
print(users['name'])
print(users['country'])


#Este es un error de TypeError
# 4 + '3'
#En el ejemplo anterior, se genera un TypeError porque no podemos sumar un número a una cadena. La primera solución sería convertir la cadena a un entero o un punto flotante. 
#Otra solución sería convertir el número a una cadena (el resultado sería '43'). Sigamos la primera solución.
print("           ")
print(4 + float('3'))


# Este es un error de Error de importación
#from math import power
#No existe una función llamada potencia en el módulo de matemáticas; tiene un nombre diferente: pow . Corrijámoslo
print("           ")
from math import pow
print(pow(2,3))


#Este es un error de Error de valor
#int('12a')
#En este caso no podemos cambiar la cadena dada a un número, debido a la letra 'a' que contiene.
print("           ")
print(int('12'))


#Este es un error de Error de división cero.
#print(1/0)
#No podemos dividir un número por cero.