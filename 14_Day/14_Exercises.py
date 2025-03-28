

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

#Utilice el bucle for para imprimir cada país en la lista de países.
print("           ")
print('Programa 4')

#Utilice for para imprimir cada nombre en la lista de nombres.
print("           ")
print('Programa 5')

#Utilice for para imprimir cada número en la lista de números.
print("           ")
print('Programa 6')




#Ejercicios: Nivel 2



#Utilice el mapa para crear una nueva lista cambiando cada país a mayúscula en la lista de países
print("           ")
print('Programa 2.1')

#Utilice el mapa para crear una nueva lista cambiando cada número por su cuadrado en la lista de números
print("           ")
print('Programa 2.2')

#Utilice el mapa para cambiar cada nombre a mayúsculas en la lista de nombres
print("           ")
print('Programa 2.3')

#Utilice el filtro para filtrar los países que contienen la palabra "tierra".
print("           ")
print('Programa 2.4')

#Utilice el filtro para filtrar países que tengan exactamente seis caracteres.
print("           ")
print('Programa 2.5')

#Utilice el filtro para filtrar los países que contengan seis letras o más en la lista de países.
print("           ")
print('Programa 2.6')

#Utilice el filtro para filtrar los países que comienzan con 'E'
print("           ")
print('Programa 2.7')

#Encadenar dos o más iteradores de lista (por ejemplo, arr.map(callback).filter(callback).reduce(callback))
print("           ")
print('Programa 2.8')

#Declare una función llamada get_string_lists que toma una lista como parámetro y luego devuelve una lista que contiene solo elementos de cadena.
print("           ")
print('Programa 2.9')

#Utilice reducir para sumar todos los números en la lista de números.
print("           ")
print('Programa 2.10')

#Utilice reduce para concatenar todos los países y producir esta oración: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa.
print("           ")
print('Programa 2.11')

#Declare una función llamada categorize_countries que devuelva una lista de países con algún patrón común (puede encontrar la lista de países en este repositorio como Countries.js (por ejemplo, 'land', 'ia', 'island', 'stan')).
print("           ")
print('Programa 2.12')

#Crea una función que devuelva un diccionario, donde las claves representan las letras iniciales de los países y los valores son la cantidad de nombres de países que comienzan con esa letra.
print("           ")
print('Programa 2.13')

#Declare una función get_first_ten_countries: devuelve una lista de los primeros diez países de la lista Countries.js en la carpeta de datos.
print("           ")
print('Programa 2.14')

#Declare una función get_last_ten_countries que devuelva los últimos diez países de la lista de países.
print("           ")
print('Programa 2.15')




#Ejercicios: Nivel 3


#Utilice el archivo Countries_data.py ( https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py ) y siga las tareas a continuación:

#Ordenar países por nombre, por capital, por población
#Clasifique los diez idiomas más hablados por ubicación.
#Clasifique los diez países más poblados.
print("           ")
print('Programa 3.1')