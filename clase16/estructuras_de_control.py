# Estructuras de control en python
# Las estructuras de control son bloques de código que permiten controlar el flujo de un programa.

# Estructuras de control condicionales
# Sintaxis de "if"
# if <condición>:
#     <bloque de código>
# else:
#     <bloque de código>
#Los if/else llevan dos puntos al final de la condición y de los bloques de código.

##Ejemplo:

grade = 10
if(grade > 5):
    print("Aprobado")
else:
    print("Reprobado")

#If con elif
#Sintaxis de "elif"
# if <condición>:
#     <bloque de código>
# elif <condición>:
#     <bloque de código>
# else:
#     <bloque de código>

#Los elif se utilizan para evaluar múltiples condiciones.

##Ejemplo:
if(grade > 5):
    print("Aprobado")
elif(grade == 5):
    print("Aprobado con 5")
else:
    print("Reprobado")

#Condicionales "and" y "or"
#Los condicionales "and" y "or" se utilizan para evaluar múltiples condiciones.

#Sintaxis de "and"
# if <condición> and <condición>:
#     <bloque de código>
# else:
#     <bloque de código>

#Sintaxis de "or"
# if <condición> or <condición>:
#     <bloque de código>
# else:
#     <bloque de código>

#El condicional "and" evalúa si ambas condiciones son verdaderas.
#El condicional "or" evalúa si al menos una de las condiciones es verdadera.

##Ejemplo:
grade = 10
if(grade > 5 and grade < 10):
    print("Aprobado")
else:
    print("Reprobado")

#Condicionales anidados
#Los condicionales anidados son condicionales dentro de otros condicionales.

##Ejemplo:
grade = 10
if(grade > 5):
    if(grade == 10):
        print("Excelente")
    else:
        print("Aprobado")
else:
    print("Reprobado")

##Ejericio: Juego de piedra, papel o tijera
#Crear un juego de piedra, papel o tijera donde el usuario pueda ingresar dos opciones y el programa determine el ganador.
#El programa debe mostrar un mensaje con el ganador.

#Sugerencia: Utilizar condicionales anidados.

#Ejemplo:
player1 = input("Player 1: ingrese piedra, papel o tijera \n").lower()
player2 = input("Player 2: ingrese piedra, papel o tijera \n").lower()

wins = {
    'piedra': 'tijera',
    'papel': 'piedra',
    'tijera': 'papel'
}

if player1 == player2:
    print("Empate")
elif player1 not in wins or player2 not in wins:
    print("Opción no válida")
elif wins[player1] == player2:
    print("Player 1 gana")
else:
    print("Player 2 gana")

