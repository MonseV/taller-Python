#Funciones
          #parámetros
""" def suma(number1, number2):
  sum = number1 + number2
  print(sum) """

     #argumentos
# suma(2, 2)

#EJERCICIO
# 3 Funciones que hagan la resta, división y multiplicación

""" def resta(number1, number2):
  res = number1 - number2
  print(res)

def division(number1, number2):
  div = number1 / number2
  print(div)

def multiplicacion(number1, number2):
  mul = number1 * number2
  print(mul)

resta(10, 5)
division(10, 5)
multiplicacion(10, 5) """


from multiprocessing.sharedctypes import Value
import random
#edad = 17
dinero = False

def vender_alcohol(edad):
  print(edad)

  if edad >= 18 and dinero:# Si esta condición no se cumple, se va directo a else
    print("Vender alcohol")

  elif edad >= 18:
    print("Te vendo alcohol, pero es fiado")

  else:# Si la condici'on no se cumple, entra aquí
    print("No vender alcohol, porque es menor de 18 años")

value = 1
while value < 2:
  value = value + 1
  edad = random.randint(5, 20) # números enteros aleatorios
  vender_alcohol(edad)