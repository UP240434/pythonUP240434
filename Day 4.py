
#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("           ")
print("Programa 1.")
first = 'Thirty '
second = 'Days '
thirty = 'Of '
fourty = 'Python'
conca = first +  second + thirty + fourty
print(conca)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("           ")
print("Programa 2.")
first = 'Coding '
second = 'For '
thirty = 'All'
conca = first +  second + thirty 
print(conca)

#Declare a variable named company and assign it to an initial value "Coding For All".
print("           ")
print("Programa 3.")
company = 'Coding for All'

#Print the variable company using print().
print("           ")
print("Programa 4.")
company = 'Coding for All'
print (company)

#Print the length of the company string using len() method and print().
print("           ")
print("Programa 5.")
company = 'Coding for All'
print (company)
print (len (company))

#Change all the characters to uppercase letters using upper() method.
print("           ")
print("Programa 6.")
company = 'Coding for All'
company.upper ()
print (company.upper ())

#Change all the characters to lowercase letters using lower() method.
print("           ")
print("Programa 7.")
company = 'Coding for All'
company.lower ()
print (company.lower ())



#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print("           ")
print("Programa 8.")
titulo = 'coding for all'
print(titulo.title())  #Coding For All
print("           ")
swap = 'COding For All'
print(swap.swapcase())  #coDING fOR aLL
swap2 = 'coding for all'
print(swap2.swapcase())  #CODING FOR ALL
print("           ")
capit = 'Coding for all'
print(capit.capitalize()) #Coding for all

#Cut(slice) out the first word of Coding For All string
print("           ")
print("Programa 9.")
company = ' Coding for All'
print (company[7:11] + company [11:15])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("           ")
print("Programa 10.")
f = 'Coding For All'
print(f.find('Coding'))  

#Replace the word coding in the string 'Coding For All' to Python.
print("           ")
print("Programa 11.")
R = 'Coding for all'
print(R.replace('Coding for all', 'Python')) # 'Python'


#Change Python for Everyone to Python for All using the replace method or other methods.
print("           ")
print("Programa 12.")
R = 'Python For Everyone'
print(R.replace('Python For Everyone', 'Python')) # 'Python'


#Split the string 'Coding For All' using space as the separator (split()) .
print("           ")
print("Programa 13.")
C = 'Coding For All'
print(C.split()) # ['thirty', 'days', 'of', 'python']


#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("           ")
print("Programa 14.")
C = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(C.split(',')) 

#What is the character at index 0 in the string Coding For All.
print("           ")
print("Programa 15.")
language = 'Coding for All'
first_letter = language[0]
print(first_letter)

#What is the last index of the string Coding For All.
print("           ")
print("Programa 16.")
language = 'Coding for ALL'
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

#What character is at index 10 in "Coding For All" string.
print("           ")
print("Programa 17.")
language = 'Coding for All'
ten = language[10]
print(ten)


#Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("           ")
print("Programa 18.")
language = 'Python For Everyone'
first_word = language[0:3] 
m_word= language[7:8]
last_three = language[10:12]
print(first_word, m_word, last_three)


#Create an acronym or an abbreviation for the name 'Coding For All'.
print("           ")
print("Programa 19.")
language = 'Python For All'
first_word = language[0:3] 
m_word= language[7:8]
last_three = language[10:12]
print(first_word, m_word, last_three)



#Use index to determine the position of the first occurrence of C in Coding For All.
print("           ")
print("Programa 20.")
f = 'Coding For All'
print(f.find('C'))  

#Use index to determine the position of the first occurrence of F in Coding For All.
print("           ")
print("Programa 21.")
f = 'Coding For All'
print(f.find('F'))  

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("           ")
print("Programa 22.")
u = 'Coding for All'
print(u.rfind('l')) 

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
#'You cannot end a sentence with because because because is a conjunction'
print("           ")
print("Programa 23.")
f = 'You cannot end a sentence with because because because is a conjunction'
print(f.find('because'))  

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 
#'You cannot end a sentence with because because because is a conjunction'
print("           ")
print("Programa 24.")
ur = 'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(ur.rindex(sub_string,))  #En este marca error si pones un numero incorrecto para comproar donde esta una palabra.

#Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print("           ")
print("Programa 25.")
eliminate = ' You cannot end a sentence with because because because is a conjunction'
print (eliminate[0:31] + eliminate[-17:])

#Find the position of the first occurrence of the word 'because' in the following sentence: 
#'You cannot end a sentence with because because because is a conjunction'
print("           ")
print("Programa 26.")
f = 'You cannot end a sentence with because because because is a conjunction'
print(f.find('because'))  

#Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print("           ")
print("Programa 27.")
eliminate = ' You cannot end a sentence with because because because is a conjunction'
print (eliminate[0:31] + eliminate[-17:])

#Does ''Coding For All' start with a substring Coding?
print("           ")
print("Programa 28.")
inicia = 'Coding for All'
print(inicia.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
print("           ")
print("Programa 29.")
termina = 'Coding for All'
print(termina.endswith('Coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("           ")
print("Programa 30.")
inicio_y_final = '   Coding For All      '
print(inicio_y_final.strip(' '))

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
print("           ")
print("Programa 31.")
cual_variable = '30DaysOfPython'
print(cual_variable .isidentifier())
es_valida = 'hirty_days_of_python'
print(es_valida .isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
# Join the list with a hash with space string.
print("           ")
print("Programa 32.")
libreria = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (libreria)
print(formated_string)


#Use the new line escape sequence to separate the following sentences.
print("           ")
print("Programa 33.") 
print('I am enjoying this challenge. \nI just wonder what is next')

#Use a tab escape sequence to write the following lines.
print("           ")
print("Programa 34.")
print('Name\t\tAge\tCountry\t\tCity')
print('Asabeneh\t250\tFinland\t\tHelsinki')

#Use the string formatting method to display the following:
print("           ")
print("Programa 35.")
radio= 10
pi = 3.14
area = pi * radio ** 2
fortmato= 'The area of a circle with a radius {} is {:.2f}.'.format(radio, area) 
print(fortmato)

#Make the following using string formatting methods:
print("           ")
print("Programa 36.")
a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
