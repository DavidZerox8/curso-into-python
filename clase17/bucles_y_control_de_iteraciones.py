#bucles y control de iteraciones

#bucle while: Es un bucle que se repite mientras una condicion sea verdadera (True)
#while condicion:
#    bloque de codigo
#    bloque
#    bloque

#contador = 0
#while contador < 10:
#    print(contador)
#    contador += 1

#bucle for: Es un bucle que se repite una cantidad de veces determinada
#for variable in lista:
#    bloque de codigo

#Ejemplo for normal
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista:
    print("numero es igual a: " , numero)

#Ejemplo for con range: range es una funcion que genera una lista de numeros en un rango determinado
for numero in range(3,10):
    print("- numero es igual a: ", numero)

#Ejemlo for con if
frutas = ["manzana", "pera", "uva", "sandia", "melon", "platano"]
for fruta in frutas:
    if fruta == "uva":
        print("La fruta es uva")
    else:
        print("La fruta no es uva, es", fruta)

#ejemplo while con if
contador = 0
while contador < 10:
    if contador == 5:
        print("El contador es igual a 5")
    else:
        print("El contador no es igual a 5, es", contador)
    contador += 1

#ejemplo for con break
for numero in range(10):
    if numero == 5:
        break
    print("numero es igual a: ", numero)

#ejemplo for con continue
for numero in range(10):
    if numero == 5:
        continue
    print("numero es igual a: ", numero)