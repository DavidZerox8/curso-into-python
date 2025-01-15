name = 'Chibiña'
name = 'Chibiña'
name = '''Chibiña'''

name_alt = '''
Chibiña

Pelupe'''

print(name)
print(name_alt)

#Concat
name = 'Chibiña'
last_name = 'Pelupe'
full_name = name + ' ' + last_name
print(full_name)

#multiply
#Show the name 3 times
print(name * 3)

#length
#Show the name length
print(len(name))

#slicing
#Show the first character
print(name[0])

#String methods

#upper()
#Show the name in uppercase
print(name.upper())

#lower()
#Show the name in lowercase
print(name.lower())

#capitalize()
#Show the name with the first letter in uppercase
print(name.capitalize())

#title()
#Show the name with the first letter of each word in uppercase
print(name.title())

#count()
#Show the number of 'i' in the name
print(name.count('i'))

#find()
#Show the position of the first 'i' in the name
print(name.find('i'))

#replace()
#Replace 'i' with 'o'
print(name.replace('i', 'o'))

#split()
#Split the name by 'i'
print(name.split('i'))

#join()
#Join the name with 'La'
print('La '.join(name))

#format()
#Show the name using format method
print('Hola, mi nombre es {}'.format(name))

#f-strings
#Show the name using f-strings method
print(f'Hola, mi nombre es {name}')

#strip()
#Remove the spaces from the name
name = '   Chibiña   '
print(name.strip())

#lstrip()
#Remove the spaces from the left of the name
print(name.lstrip())

#rstrip()
#Remove the spaces from the right of the name
print(name.rstrip())

#startswith()
#Check if the name starts with 'C'
print(name.startswith('C'))

#endswith()
#Check if the name ends with 'a'
print(name.endswith('a'))

#isalnum()
#Check if the name is alphanumeric
print(name.isalnum())

#isalpha()
#Check if the name is alphabetic
print(name.isalpha())

#isdigit()
#Check if the name is a digit
print(name.isdigit())

#isspace()
#Check if the name is a space
print(name.isspace())

#istitle()
#Check if the name is a title
print(name.istitle())

#isupper()
#Check if the name is uppercase
print(name.isupper())

#islower()
#Check if the name is lowercase
print(name.islower())

#istitle()
#Check if the name is a title
print(name.istitle())

#isnumeric()
#Check if the name is numeric
print(name.isnumeric())

#isprintable()
#Check if the name is printable
print(name.isprintable())

#isidentifier()
#Check if the name is an identifier
print(name.isidentifier())

#isascii()
#Check if the name is ascii
print(name.isascii())

#isdecimal()
#Check if the name is decimal
print(name.isdecimal())
