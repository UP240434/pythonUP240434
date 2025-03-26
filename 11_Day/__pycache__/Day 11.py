
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
def sum_all_nums():
    m = [1,2,3,4,5]
    n = sum(m,0)
    print(n)
sum_all_nums()

#La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit .
print("           ")
print('Programa 4')
def add_Celsius ():
    c = 45
    total = (c * 9/5) + 32
    print(total, " Grados Farenheit")
add_Celsius()

#Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.
print("           ")
print('Programa 5')


    
#Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal
print("           ")
print('Programa 6')


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
def reverse_list():
    fruits = ['1', '2', '3', '4']      
    for fruit in fruits:
     print(fruit)
(reverse_list())




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

print(sum_of_numbers(68))

#Declara una función llamada suma_de_impares. Esta función toma un parámetro numérico y suma todos los números impares en ese rango.
print("           ")
print('Programa 14')


#Declara una función llamada suma_de_números_pares. Esta función toma un parámetro numérico y suma todos los números pares en ese rango.
print("           ")
print('Programa 15')



#Ejercicios: Nivel 2

#Declare una función llamada evens_and_odds. Esta función toma un entero positivo como parámetro y cuenta el número de pares e impares en el número.
print("           ")
print('Programa 2.1')
#Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número.
print("           ")
print('Programa 2.2')
#Llama a tu función is_empty , toma un parámetro y verifica si está vacío o no
print("           ")
print('Programa 2.3')

#Escriba diferentes funciones que acepten listas. Estas funciones deben calcular la media, la mediana, la moda, el rango, la varianza y la desviación estándar (desviación estándar).
print("           ")
print('Programa 2.4')




#Ejercicios: Nivel 3

#Escriba una función llamada is_prime, que verifique si un número es primo.
print("           ")
print('Programa 3.1')

#Escriba una función que verifique si todos los elementos son únicos en la lista.
print("           ")
print('Programa 3.2')
#Escriba una función que verifique si todos los elementos de la lista son del mismo tipo de datos.
print("           ")
print('Programa 3.3')
#Escriba una función que verifique si la variable proporcionada es una variable de Python válida
print("           ")
print('Programa 3.4')
#Vaya a la carpeta de datos y acceda al archivo Countries-data.py.
##Crea una función llamada "los países más poblados". Debería devolver los 10 o 20 países más poblados en orden descendente.
print("           ")
print('Programa 3.5')