""" edad = "30"
estatura = "1.58"

resultado1 = edad + estatura #concatenación de Strings

print(edad)
print(estatura)
print(resultado1)

print("Después de esto, se aplica la conversión")

edad = int(edad)
estatura = float(estatura)

resultado2 = edad + estatura

print(edad)
print(estatura)
print(resultado2) """

#Otros
#str()
#bool("")

#input() -> esto siempre te va a dar cadenas
""" edad = input("Ingresa tu edad: ")
edad = int(edad)
estatura = input("Ingresa tu estatura: ")
estatura = float(estatura)
resultado = edad + estatura
print(resultado) """


""" def presentation():
  name = input("Nombre: ")

  age = input("Edad: ")
  age = int(age)

  height = input("Estatura: ")
  height = float(height)

  #f -> permite integrar las varibles a una cadena
  print(f"Hola, soy {name} tengo {age} años y mido {height}")

presentation() """



#EJERCICIO
#Utilizar las funciones que se habian hecho y
#pedir los parámetros dentro de la función


number1 = input("Dame el primer numero: ")
number1 = float(number1)

number2 = input("Dame el segundo numero: ")
number2 = float(number2)


def sumar():
  sum = number1 + number2
  print(f"La suma de {number1} y {number2} da como resultado {sum}")

def resta():
  res = number1 - number2
  print(f"La resta de {number1} y {number2} da como resultado {res}")

def division():
  div = number1 / number2
  print(f"La division de {number1} y {number2} da como resultado {div}")

def multiplicacion():
  mul = number1 / number2
  print(f"La multiplicacion de {number1} y {number2} da como resultado {mul}")

sumar()
resta()
division()
multiplicacion()