countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from functools import reduce





#Ejercicios: Nivel 1


#Explique la diferencia entre mapa, filtro y reducción.
print("           ")
print('Programa 1')
print('La función map() es una función incorporada que toma una función y un iterable como parámetros.') 
print('Lo que hace map es iterar sobre una lista. Por ejemplo, cambia los nombres a mayúsculas y devuelve una nueva lista con todos los elementos')
print("           ")
print('La función filter() llama a la función especificada, que devuelve un valor booleano para cada elemento del iterable (lista) especificado.')
print('Filtra los elementos que cumplen los criterios de filtrado, imprimiendo solo ciertos elementos.')
print("           ")
print('La función reduce() se define en el módulo functools y debemos importarla desde este módulo. Al igual que map y filter, acepta dos parámetros: una función y un iterable.')
print('Sin embargo, no devuelve otro iterable, sino un único valor, dando valores nuevos a los originales.')

#Explique la diferencia entre función de orden superior, cierre y decorador.
print("           ")
print('Programa 2')
print('Una función puede tomar una o más funciones como parámetros')
print('Una función puede ser devuelta como resultado de otra función')
print('Una función se puede modificar')
print('Se puede asignar una función a una variable')

print("           ")
print('Python permite que una función anidada acceda al ámbito externo de la función que la encapsula. Esto se conoce como cierre.')
print('Veamos cómo funcionan los cierres en Python. En Python, un cierre se crea anidando una función dentro de otra función que la encapsula y luego devolviendo la función interna. ')

print("           ")
print('Un decorador es un patrón de diseño en Python que permite al usuario añadir nuevas funciones a un objeto existente sin modificar su estructura.')
print('Los decoradores suelen llamarse antes de la definición de la función que se desea decorar.')
print('Para crear una función decoradora, necesitamos una función externa con una función contenedora interna.')
print('La mayoría de las veces necesitamos que nuestras funciones tomen parámetros, por lo que es posible que necesitemos definir un decorador que acepte parámetros.')

#Defina una función de llamada antes de map, filter o reduce, vea los ejemplos.
print("           ")
print('Programa 3')
def mapa(num):
    return num ** 3
print(list(map(mapa, numbers)))

def filtro(name):
    if name[0] in 'AE':
        return True
    return False
print(list(filter(filtro, names)))

def suma_de_mapa(num1, num2):
    return num1 + num2
print(reduce(suma_de_mapa, list(map(mapa, numbers))))


#Utilice el bucle for para imprimir cada país en la lista de países.
print("           ")
print('Programa 4')
for i in countries:
    print(i)


#Utilice for para imprimir cada nombre en la lista de nombres.
print("           ")
print('Programa 5')
for i in names:
    print(i)

#Utilice for para imprimir cada número en la lista de números.
print("           ")
print('Programa 6')
for i in numbers:
    print(i)




#Ejercicios: Nivel 2


#Utilice el mapa para crear una nueva lista cambiando cada país a mayúscula en la lista de países
print("           ")
print('Programa 2.1')
def upper(countries):
    return countries.upper()
print(list(map(upper, countries)))


#Utilice el mapa para crear una nueva lista cambiando cada número por su cuadrado en la lista de números
print("           ")
print('Programa 2.2')
def square(num):
    return num ** 2
print(list(map(square, numbers)))

#Utilice el mapa para cambiar cada nombre a mayúsculas en la lista de nombres
print("           ")
print('Programa 2.3')
print(list(map(upper, names)))

#Utilice el filtro para filtrar los países que contienen la palabra "tierra".
print("           ")
print('Programa 2.4')
def land(countries):
    if 'land' in countries:
        return True
    return False
print(list(filter(land, countries)))

#Utilice el filtro para filtrar países que tengan exactamente seis caracteres.
print("           ")
print('Programa 2.5')
def seis(countries):
    if len(countries) == 6:
        return True
    return False
print(list(filter(seis, countries)))

#Utilice el filtro para filtrar los países que contengan seis letras o más en la lista de países.
print("           ")
print('Programa 2.6')
def seis_o_mas(countries):
    if len(countries) >= 6:
        return True
    return False
print(list(filter(seis_o_mas, countries)))

#Utilice el filtro para filtrar los países que comienzan con 'E'
print("           ")
print('Programa 2.7')
def E(countries):
    if countries[0] == 'E':
        return True
    return False
print(list(filter(E, countries)))

#Encadenar dos o más iteradores de lista (por ejemplo, arr.map(callback).filter(callback).reduce(callback))
print("           ")
print('Programa 2.8')


#Declare una función llamada get_string_lists que toma una lista como parámetro y luego devuelve una lista que contiene solo elementos de cadena.
print("           ")
print('Programa 2.9')
def string(string):
    return str(string)

def get_string_lists(cadena):
    return list(map(string, cadena))
print(get_string_lists(numbers))


#Utilice reducir para sumar todos los números en la lista de números.
print("           ")
print('Programa 2.10')
def suma(x, y):
    return int(x) + int(y)
print(reduce(suma, numbers))

#Utilice reduce para concatenar todos los países y producir esta oración: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa.
print("           ")
print('Programa 2.11')
def concatenar_countries(x, y):
    if x == "Estonia, Finland, Sweden, Denmark, Norway" and y == "Iceland":
        return x + ", and " + y
    else:
        return x + ", " + y
print(reduce(concatenar_countries, countries) + " are north European countries")

#Declare una función llamada categorize_countries que devuelva una lista de países con algún patrón común (puede encontrar la lista de países en este repositorio como Countries.js 
#(por ejemplo, 'land', 'ia', 'island', 'stan')).
print("           ")
print('Programa 2.12')
import paises as p
paises = p.countries 
print(list(filter(land, paises)))



#Crea una función que devuelva un diccionario, donde las claves representan las letras iniciales de los países y los valores son la cantidad de nombres de países que comienzan 
#con esa letra.
print("           ")
print('Programa 2.13')
keys = []
keys = [i[0] for i in paises if i[0] not in keys]

def contarcountry(contador):
    return sum([True for i in paises if i[0].startswith(contador)])

values = [contarcountry(l) for l in keys]

print(dict(zip(keys, values)))

#Declare una función get_first_ten_countries: devuelve una lista de los primeros diez países de la lista Countries.js en la carpeta de datos.
print("           ")
print('Programa 2.14')
def get_first_ten_countries():
    return paises[:10]
print(get_first_ten_countries())


#Declare una función get_last_ten_countries que devuelva los últimos diez países de la lista de países.
print("           ")
print('Programa 2.15')
def get_last_ten_countries():
    return paises[-1:-11:-1]
print(get_last_ten_countries())



#Ejercicios: Nivel 3


#Utilice el archivo Countries_data.py ( https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py ) y siga las tareas a continuación:

#Ordenar países por nombre, por capital, por población
#Clasifique los diez idiomas más hablados por ubicación.
#Clasifique los diez países más poblados.
print("           ")
print('Programa 3.1')

from countries_data import countries


paises_ordenados_por_nombre = sorted(countries, key=lambda x: x['name'])
paises_ordenados_por_capital = sorted(countries, key=lambda x: x.get('capital', ''))
paises_ordenados_por_poblacion = sorted(countries, key=lambda x: x['population'], reverse=True)
diez_mas_poblados = paises_ordenados_por_poblacion[:10]


from collections import defaultdict

language_count = defaultdict(int)
for country in countries:
    for language in country.get('languages', []):
        language_count[language] += 1


diez_mas_hablados = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]

print("Países ordenados por nombre:", [country['name'] for country in paises_ordenados_por_nombre])
print("                                                                                             ")
print("Países ordenados por capital:", [country['name'] for country in paises_ordenados_por_capital])
print("                                                                                             ")
print("Países ordenados por población:", [(country['name'], country['population']) for country in paises_ordenados_por_poblacion])
print("                                                                                             ")
print("Diez idiomas más hablados por ubicación:", diez_mas_hablados )
print("                                                                                             ")
print("Diez países más poblados:", [(country['name'], country['population']) for country in diez_mas_poblados])
print("revisado")