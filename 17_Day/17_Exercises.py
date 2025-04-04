
#names = ['Finlandia', 'Suecia', 'Noruega', 'Dinamarca', 'Islandia', 'Estonia', 'Rusia']. 
#Descomprima los primeros cinco países y almacénelos en una variable nordic_countries, almacene Estonia y Rusia en es y ru respectivamente.
print("           ")
print('Programa 1')
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
try:
    *nordic_countries, es, ru = names
    print(nordic_countries, es, ru)
except Exception as e:
    print(e)