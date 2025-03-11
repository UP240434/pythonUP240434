#Declare an empty list
print("           ")
print('Programa 1')
lista_vacia = list() # this is an empty list, no item in the list
print(len(lista_vacia)) # 0

#Declare a list with more than 5 items
print("           ")
print('Programa 2')
vegetales = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']  
print (vegetales)


#Find the length of your list
print("           ")
print('Programa 3')
vegetales = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']  
print (len(vegetales))


#Get the first item, the middle item and the last item of the list
print("           ")
print('Programa 4')
vegetales = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']  
primera_verdura = vegetales[0] # we are accessing the first item using its index
print(primera_verdura)     
enmedio_verdura = vegetales[2]
print(enmedio_verdura)   
ultima_verdura = vegetales[4]
print(ultima_verdura) 


#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
print("           ")
print('Programa 5')
mixed_data_types =  [{'Name':'Gael Quirarte Sandoval', 'Age':'18', 'Height':'1.73', 'Marital Status':'Single','Adress':'Dr. Narciso Gonzalez 22A'}] 
# list containing different data types
print (mixed_data_types)


#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print("           ")
print('Programa 6')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple','IBM', 'ORACLE', 'Amazon']


#Print the list using print()
print("           ")
print('Programa 7')
print (it_companies )


#Print the number of companies in the list
print("           ")
print('Programa 8')
print (len(it_companies))


#Print the first, middle and last company
print("           ")
print('Programa 9')
primera_company = it_companies[0] # we are accessing the first item using its index
print(primera_company)     
enmedio_company = it_companies[2]
print(enmedio_company)   
ultima_company= it_companies[4]
print(ultima_company) 


#Print the list after modifying one of the companies
print("           ")
print('Programa 10')
it_companies[5] = 'Samsung'
print(it_companies)   


#Add an IT company to it_companies
print("           ")
print('Programa 11')
it_companies.append('WhatsApp')
print(it_companies )  


#Insert an IT company in the mid
print("           ")
print('Programa 12')
it_companies.insert(4, 'Instagram') # insert apple between orange and mango
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
print("           ")
print('Programa 13')
it_companies[0] = 'FACEBOOK'
print(it_companies)   


#Join the it_companies with a string '#;  '
print("           ")
print('Programa 14')
it_companies = ['#Facebook, #Google, #Microsoft, #Apple,#IBM, #ORACLE, #Amazon']
print (it_companies)


#Check if a certain company exists in the it_companies list
print("           ")
print('Programa 15')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple','IBM', 'ORACLE', 'Amazon']
print(it_companies.index('Google')) 


#Sort the list using sort() method
print("           ")
print('Programa 16')
it_companies.sort() #Orden Alfabetico
print(it_companies)    


#Reverse the list in descending order using reverse() method
print("           ")
print('Programa 17')
it_companies.sort(reverse=True)
print(it_companies)


#Slice out the first 3 companies from the list
print("           ")
print('Programa 18')
First_companies = it_companies[0:3]
print(First_companies)


#Slice out the last 3 companies from the list
print("           ")
print('Programa 19')
Last_companies = it_companies[-3:]
print(Last_companies)



#Slice out the middle IT company or companies from the list
print("           ")
print('Programa 20')
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple','IBM', 'ORACLE', 'Amazon']
del it_companies[2:5] 
print(it_companies)

#Remove the first IT company from the list
print("           ")
print('Programa 21')
del it_companies[0] 
print(it_companies)


#Remove the middle IT company or companies from the list
print("           ")
print('Programa 22')
del it_companies[1] 
print(it_companies)


#Remove the last IT company from the list
print("           ")
print('Programa 23')
it_companies.pop()
print(it_companies) 

#Remove all IT companies from the list
print("           ")
print('Programa 24')
it_companies.clear()
print(it_companies)  

#Destroy the IT companies list
print("           ")
print('Programa 25')
it_companies= list()
print(it_companies)  



#Join the following lists:
print("           ")
print('Programa 26')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end)
print(back_end)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
print("           ")
print('Programa 27')
front_end.extend(back_end)
print('List:', front_end)

print("           ")
full_stack = front_end.copy()
print(full_stack)  

print("           ")
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack) 





#EXERCISES: LEVEL 2.



#The following is a list of 10 students ages:

#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]



#Sort the list and find the min and max age
print("           ")
print("           ")
print("           ")
print('Programa 2.1')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 

#Add the min age and the max age again to the list
print("           ")
print('Programa 2.3')
Add_numbers = [19,26]
integers = ages + Add_numbers
print(integers)

#Find the median age (one middle item or two middle items divided by two)
print("           ")
print('Programa 2.4')
median_age = ages[4:6]
print(median_age)

#Find the average age (sum of all items divided by their number )
print("           ")
print('Programa 2.5')
average_age = [(19+ 22+ 19+ 24+ 20+ 25+ 26+ 24+ 25+ 24)/2]
print(average_age)


#Find the range of the ages (max minus min)
print("           ")
print('Programa 2.6')
Range_ages = (26-19)
print (Range_ages)


#Compare the value of (min - average) and (max - average), use abs() method
print("           ")
print('Programa 2.7')
average_age = (19+ 22+ 19+ 24+ 20+ 25+ 26+ 24+ 25+ 24)/2
min = 19
max = 26
valor1 = (min)-(average_age)
valor2 = (max-average_age)
print(abs(valor1))
print(abs(valor2))


#Find the middle country(ies) in the countries list
print("           ")
print('Programa 3.1')
import paises as p
paises = p.countries 
print(len(paises))

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
print("           ")
print('Programa 3.2')
print("           ")
primera= paises[0:96] 
segunda= paises[96:193] 
print(primera)
print("           ")
print("           ")
print("           ")
print(segunda)
print("           ")
print("           ")
print("           ")

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
print("           ")
print('Programa 3.3')
paises.remove('China')
paises.remove('Russia')
paises.remove('United States')
paises_removidos = ['China', 'Russia', 'USA']
print(paises_removidos )
print("           ")
print(len(paises))
print("           ")
print('Scandic Countries:')
print("           ")
print("           ")
print("           ")
print(paises)
