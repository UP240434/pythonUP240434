
#Filtrar solo los negativos y ceros en la lista usando la comprensión de listas
print("           ")
print('Programa 1')
def negative_list():
    numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
    return [x for x in numeros if x <= 0]
print(negative_list())

#Aplana la siguiente lista de listas de listas a una lista unidimensional:
print("           ")
print('Programa 2')
def unidimensional_list():
    lista_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    return [x for num in lista_de_listas for num2 in num for x in num2]
print(unidimensional_list())

#Usando la comprensión de listas, cree la siguiente lista de tuplas:
print("           ")
print('Programa 3')
def genera_lista_de_tuplas():
    tabla = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
    for tupla in tabla:
        print(tupla)
print(genera_lista_de_tuplas())

#Aplana la siguiente lista a una nueva lista:
print("           ")
print('Programa 4')
def aplana_lista():
    paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    return [[num2[0].upper(), num2[0].upper()[:3], num2[1].upper()] for num in paises for num2 in num]
print(aplana_lista())


#Cambie la siguiente lista a una lista de diccionarios:
print("           ")
print('Programa 5')
def lista_a_diccionario():
    paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    paises = [[sub2[0].upper(), sub2[1].upper()] for sub in paises for sub2 in sub]
    paises = [x for sub in paises for x in sub]
    llave = ["country", "city"]
    return [{llave[0]: paises[ciudad], llave[1]: paises[ciudad + 1]} for ciudad in range(0, len(paises), 2)]
for diccionario in lista_a_diccionario():
    print(diccionario)

#Cambie la siguiente lista de listas a una lista de cadenas concatenadas:
print("           ")
print('Programa 6')
def lista_concatenada():
    nombres_apellido = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    concatena = [x for num in nombres_apellido for num2 in num for x in num2]
    return [concatena[i] + ' ' + concatena[i + 1] for i in range(0, len(concatena), 2)]
print(lista_concatenada())

#Escriba una función lambda que pueda resolver una pendiente o una intersección con el eje y de funciones lineales.
print("           ")
print('Programa 7')
equacion = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_interseccion = lambda x1, y1, x2, y2: y1 - equacion(x1, y1, x2, y2) * x1
print(y_interseccion(1,2,3,4))