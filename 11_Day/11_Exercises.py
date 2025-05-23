import math
import re
import sys

#Ejercicios Nivel 1

#Declare la función add_two_numbers . Esta función acepta dos parámetros y devuelve una suma.
print("           ")
print('Programa 1')
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

#El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule área_del_círculo .
print("           ")
print('Programa 2')
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

#Escriba una función llamada add_all_nums que tome cualquier número de argumentos y los sume. Compruebe si todos los elementos de la lista son de tipo numérico. 
# De no ser así, proporcione una respuesta razonable.
print("           ")
print('Programa 3')
def add_all_nums():
    m = [1,2,3,4,5]
    n = sum(m,0)
    print(n)
    print(type(n))
add_all_nums()

#La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit .
print("           ")
print('Programa 4')
def convert_celsius_to_fahrenheit ():
    c = 45
    total = (c * 9/5) + 32
    print(total, " Grados Farenheit")
convert_celsius_to_fahrenheit()

#Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.
print("           ")
print('Programa 5')
def check_season(mes):
    mes = str(input('Month:'))
    if mes in ["September", "October", "November"]:
        print("Autumn")
    if mes in ["December", "January", "February"]:
        print("Winter")
    if mes in ["March", "April", "May"]:
        print("Spring")
    if mes in ["Jun", "July", "August"]:
        print("Summer")
check_season('mes')

    
#Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal
print("           ")
print('Programa 6')
def calculate_slope(m):
    x1 = 2
    x2 = 6
    y1 = 2
    y2 = 10
    m = (y2 - y1) / (x2 - x1)
    return m
print(calculate_slope('valor'))

#La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escriba una función que calcule el conjunto solución de una ecuación cuadrática,
# solve_quadratic_eqn .
print("           ")
print('Programa 7')
def solve_quadratic_eqn  (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))


#Declara una función llamada print_list. Esta toma una lista como parámetro e imprime cada elemento de la lista.4print("           ")
print("           ")
print('Programa 8')
def print_list():
    fruits = ['1', '2', '3', '4']      
    for fruit in fruits:
     print(fruit)

print(print_list())

#Declare una función llamada reverse_list. Esta recibe un array como parámetro y devuelve su valor inverso (usando bucles).
print("           ")
print('Programa 9')
def reverse_list():
    fruits = ['1', '2', '3', '4']
    fruits.reverse()        
    for fruit in fruits:
     print(fruit)
(reverse_list())

#Declare una función llamada capitalize_list_items. Esta toma una lista como parámetro y devuelve una lista de elementos en mayúsculas.
print("           ")
print('Programa 10')
def capitalize_list_items(lista): 
    listaMayus = []
    for valor in lista:
        listaMayus.append(valor.upper())
   
    return listaMayus

fruits = ['banana ' ,'manzana ', 'uva ', 'zanahoria']
frutasMayus = capitalize_list_items(fruits)
print(frutasMayus)


#Declara una función llamada add_item. Esta toma como parámetros una lista y un elemento. Devuelve una lista con el elemento añadido al final.
print("           ")
print('Programa 11')
def add_item(lista): 
    frutas.append('apple') 
frutas= ['banana', 'orange', 'mango', 'lemon']
add_item(frutas)   
print(frutas)  

#Declara una función llamada remove_item. Esta toma como parámetros una lista y un elemento. Devuelve una lista con el elemento eliminado.
print("           ")
print('Programa 12')
def remove_item(lista): 
    frutas.pop() 
frutas= ['banana', 'orange', 'mango', 'lemon']
remove_item(frutas)   
print(frutas)

#Declara una función llamada suma_de_números. Esta función toma un parámetro numérico y suma todos los números en ese rango.
print("           ")
print('Programa 13')
def sum_of_numbers(n):
    total = 0
    for i in range(n):
        total += i
    return total
print(sum_of_numbers(11))

#Declara una función llamada suma_de_impares. Esta función toma un parámetro numérico y suma todos los números impares en ese rango.
print("           ")
print('Programa 14')
def suma_de_impares(impar):
    suma_de_impar_numeros = 0
    for i in range(impar + 1):
        if i % 2 == 1:
            suma_de_impar_numeros += i
    return suma_de_impar_numeros
print(suma_de_impares(10))


#Declara una función llamada suma_de_números_pares. Esta función toma un parámetro numérico y suma todos los números pares en ese rango.
print("           ")
print('Programa 15')
def suma_de_numeros_pares(par):
    suma_de_numeros_pares = 0
    for i in range(par + 1):
        if i % 2 == 0:
            suma_de_numeros_pares += i
    return suma_de_numeros_pares
print(suma_de_numeros_pares(11))

#Ejercicios: Nivel 2

#Declare una función llamada evens_and_odds. Esta función toma un entero positivo como parámetro y cuenta el número de pares e impares en el número.
print("           ")
print('Programa 2.1')
def even_and_odds (number):
    odds = 0
    even = 0
    for i in range (0,number +1):
        if i % 2 == 0:
            even = even +1
        else :
            odds = odds + 1
    return {"evens":even,"odds":odds}
print(even_and_odds(number = 100))

#Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número.
print("           ")
print('Programa 2.2')
def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado
print(factorial(3))


#Llama a tu función is_empty , toma un parámetro y verifica si está vacío o no
print("           ")
print('Programa 2.3')
def is_empty(cadena):
    cadena == ""
    long = len(cadena)
    if (long == 0):
        print("La cadena esta vacía");
    else:
         print("La cadena no esta vacía");
is_empty("")


#Escriba diferentes funciones que acepten listas. Estas funciones deben calcular la media, la mediana, la moda, el rango, la varianza y la desviación estándar (desviación estándar).
print("           ")
print('Programa 2.4')
from statistics import median, median, mode, variance, stdev
lista = [1, 2, 3, 4, 5]
def calcular_media (lista):
    return median(lista)
def calcular_mediana (lista):
    return median(lista)
def calcular_moda (lista):
    return mode(lista)
def calcular_rango (lista):
    return max(lista) - min(lista)
def calcular_varianza (lista):
    return variance(lista)
def calcular_destiacion_estandar (lista):
    return stdev(lista)
print("Media:",calcular_media(lista))
print("Mediana:",calcular_mediana(lista))
print("Moae:",calcular_moda(lista))
print("Rango:",calcular_rango(lista))
print("Varianza:",calcular_varianza(lista))
print("Desviacion estandar:",calcular_destiacion_estandar (lista))

#Ejercicios: Nivel 3

#Escriba una función llamada is_prime, que verifique si un número es primo.
print("           ")
print('Programa 3.1')
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))

#Escriba una función que verifique si todos los elementos son únicos en la lista.
print("           ")
print('Programa 3.2')
def unico_list(unico_list):
    return len(set(unico_list)) == len(unico_list)
print(unico_list([1,2,3,4,5]))

#Escriba una función que verifique si todos los elementos de la lista son del mismo tipo de datos.
print("           ")
print('Programa 3.3')
def mismo_type(lista):
    list = iter(lista)
    first_type = type(next(list))
    return first_type if all((type(x) is first_type) for x in list) else False
print(mismo_type([1,2,3,4,5]))

#Escriba una función que verifique si la variable proporcionada es una variable de Python válida
print("           ")
print('Programa 3.4')
def valide_variable (variable):
     if variable.isidentifier():
         return True
     else:
         return False
print('¿Es Valida?',valide_variable('Gael'))
 

#Vaya a la carpeta de datos y acceda al archivo Countries-data.py.
#Crea una función llamada "los idiomas más hablados del mundo". Debería devolver los 10 o 20 idiomas más hablados del mundo en orden descendente.
##Crea una función llamada "los países más poblados". Debería devolver los 10 o 20 países más poblados en orden descendente.
print("           ")
print('Programa 3.5')
import countries_data as cd
countrieslist = cd.countries
total_languages = []
for i in countrieslist:
    total_languages.extend(i["languages"])
cuenta = {}
for i in total_languages:
    cuenta[i] = cuenta.get(i, 0) + 1


def los_mas(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))
print("           ")
print('Los 20 idiomas mas hablados del mundo')
cuenta = los_mas(cuenta, True)
for i in list(cuenta.items())[:20]:
    print(i)
print("           ")
print('Los 20 paises mas poblados del mundo')
poblacion = {}
for i in countrieslist:
    poblacion[i["name"]] = i["population"]
poblacion = los_mas(poblacion, True)
for i in list(poblacion.items())[:20]:
    print(i)

print("revisado")