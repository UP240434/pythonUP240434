import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
char_lista = []
char_lista[:0] = chars

#Ejercicios: Nivel 1

#Escriba una función que genere un random_user_id de seis dígitos/caracteres.
print("           ")
print('Programa 1')
def random_user_id():
    genera = ''
    for _ in range(6):
        genera += random.choice(char_lista)
    return genera
print(random_user_id())

#Modifique la tarea anterior. Declare una función llamada user_id_gen_by_user. No acepta parámetros, pero acepta dos entradas mediante input().
# Una de las entradas es el número de caracteres y la otra, el número de ID que se generarán.
print("           ")
print('Programa 2')
def user_id_gen_by_user():
    charsize = int(input('Enter Character Size: '))
    charid = int(input('Enter how many user ids to generate: '))
    for _ in range(charid):
        genera = ''.join([random.choice(char_lista) for _ in range(charsize)])
        print(genera)
print(user_id_gen_by_user())

#Escriba una función llamada rgb_color_gen. Esta generará colores RGB (tres valores de 0 a 255 cada uno).
print("           ")
print('Programa 3')
def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b = str(random.randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"
print(rgb_color_gen())

#Ejercicios: Nivel 2

#Escriba una función list_of_hexa_colors que devuelva cualquier número de colores hexadecimales en una matriz (seis números hexadecimales escritos después de #. 
#El sistema de numeración hexadecimal está formado por 16 símbolos, del 0 al 9 y las primeras 6 letras del alfabeto, af. Consulte la tarea 6 para ver ejemplos de salida).
print("           ")
print('Programa 2.1')
def list_of_hexa_colors(algun =0):
    if algun == 0:
        algun = random.randint(1, 10)
    hexas = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
    hexCodes = []
    for _ in range(algun):
        hexCodes.append("#" + ''.join([random.choice(hexas) for _ in range(6)]))
    return hexCodes
print(list_of_hexa_colors())

#Escriba una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz.
print("           ")
print('Programa 2.2')
def list_of_rgb_colors(algun=0):
    if algun == 0:
        algun = random.randint(1, 10)
    lista = []
    for _ in range(algun):
        lista.append(rgb_color_gen())
    return lista
print(list_of_rgb_colors())

#Escriba una función generate_colors que pueda generar cualquier cantidad de colores hexadecimales o rgb.
print("           ")
print('Programa 2.3')
def generate_colors(tipo_of_color, algun):
    if tipo_of_color == 'hexa':
        return list_of_hexa_colors(algun)
    elif tipo_of_color == 'rgb':
        return list_of_rgb_colors(algun)
    else:
        return "Invalid Input"
print(generate_colors('rgb',3))

#Ejercicios: Nivel 3
#Llama a tu función shuffle_list, toma una lista como parámetro y devuelve una lista aleatoria
print("           ")
print('Programa 3.1')
def shuffled_list(fruit):
    return random.sample(fruit, len(fruit))
print(shuffled_list(['banana', 'orange', 'mango', 'lemon']))

#Escriba una función que devuelva un array de siete números aleatorios en un rango del 0 al 9. Todos los números deben ser únicos.
print("           ")
print('Programa 3.2')
def seven_random():
    lista = []
    length = -1
    while length <= 7:
        num = random.randint(0, 9)
        if num not in lista:
            lista.append(num)
            length = len(lista)
    return lista
print(seven_random())