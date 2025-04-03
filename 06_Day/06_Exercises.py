# EXERCISES: LEVEL 1.



#Create an empty tuple
print("           ")
print('Programa 1')
empty_tuple = tuple()
print(empty_tuple)

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
print("           ")
print('Programa 2')
tupla_hermana = ('Alexa', 'Paola')
tupla_hermano = ('Hector', 'Jose')
print(tupla_hermana)
print(tupla_hermano)

#Join brothers and sisters tuples and assign it to siblings
print("           ")
print('Programa 3')
tupla_hermanos = tupla_hermana + tupla_hermano
print(tupla_hermanos)


#How many siblings do you have?
print("           ")
print('Programa 4')
print('Tengo: ',len(tupla_hermanos), ' hermanos')

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
print("           ")
print('Programa 5')
tupla_papas = ('Florencio', 'Maria')
tupla_family_members = tupla_hermana + tupla_hermano + tupla_papas
print(tupla_family_members)





print("           ")
# EXERCISES: LEVEL 2.



#Unpack siblings and parents from family_members
print("           ")
print('Programa 2.1')
tupla_hermana = ('Alexa', 'Paola')
tupla_hermano = ('Hector', 'Jose')
tupla_papas = ('Florencio', 'Maria')
tupla_family_members = tupla_hermana + tupla_hermano + tupla_papas
del tupla_family_members


#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
print("           ")
print('Programa 2.2')
frutas = ('Banana', 'Orange', 'Mango',)
vegetales = ('Tomato', 'Potato', 'Cabbage')
animales = ('Egg', 'Meat', 'Milk')
food_stuff_tp = frutas + vegetales + animales
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
print("           ")
print('Programa 2.3')
food_stuff_lt = list(food_stuff_tp)
print (food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("           ")
print('Programa 2.4')
enmedio_food= food_stuff_lt[4]
print(enmedio_food)  

#Slice out the first three items and the last three items from food_staff_lt list
print("           ")
print('Programa 2.5')
print(food_stuff_lt)
print("           ")
First_food = food_stuff_lt[0:3]
print(First_food)
print("           ")
Last_food = food_stuff_lt[-3:]
print(Last_food)
print("           ")
Ultimate_food = food_stuff_lt[3:6]
print(Ultimate_food)


#Delete the food_staff_tp tuple completely
print("           ")
print('Programa 2.6')
print(food_stuff_tp)
del food_stuff_tp


#Check if 'Estonia' is a nordic country
print("           ")
print('Programa 2.7')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

#Check if 'Iceland' is a nordic country
print("           ")
print('Programa 2.8')
print('Iceland' in nordic_countries)
print("           ")


print("revisado")