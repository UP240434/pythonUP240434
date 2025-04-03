
from datetime import datetime
from datetime import date

#Obtenga el día, mes, año, hora, minuto y marca de tiempo actuales del módulo datetime
print("           ")
print('Programa 1')
now = datetime.now()
print(now)


#Formatee la fecha actual utilizando este formato: "%m/%d/%Y, %H:%M:%S")
print("           ")
print('Programa 2')
day = now.day
month = now.month
year = now.year
hour = now.hour
min = now.minute
tstamp = now.timestamp()

t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)

#Hoy es 5 de diciembre de 2019. Cambie esta cadena de tiempo a hora.
print("           ")
print('Programa 3')
date_cadena= "5 December, 2019"
date_hora = datetime.strptime(date_cadena, "%d %B, %Y")
print(date_hora)

#Calcula la diferencia horaria entre ahora y el año nuevo.
print("           ")
print('Programa 4')
new_year = date(year = 2022, month = 1, day = 1)
today = date(year = 2021, month = 9, day = 20)
dif = new_year - today
print(dif)

#Calcula la diferencia horaria entre el 1 de enero de 1970 y la actualidad.
print("           ")
print('Programa 5')
today = date(year = 2021, month = 9, day = 20)
ene_1970 = date(year = 1970, month = 1, day = 1)
dif2 =-(today - ene_1970) 
print(dif2)

#Piensa, ¿para qué puedes usar el módulo datetime? Ejemplos:

#Análisis de series temporales
#Para obtener una marca de tiempo de cualquier actividad en una aplicación
#Agregar publicaciones a un blog
print("           ")
print('Programa 6')