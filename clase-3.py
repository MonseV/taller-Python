#Operadores Relacionales

# > devuelve true si el operador de la izq es mayor que el de la der
if 4 > 3:
  print("4 es mayor que 3")

# <     "    true "  "     "      "  " der  "   "    "   "  "  " izq
if 3 < 4:
  print("3 es menor que 4")

# == devuelve true si ambos operadores son iguales
if 4 == 4:
  print("4 es igual a 4")

# >= devuelve true si el operador de la izq es mayor o igual que el de la der
if 4 >= 3:
  print("4 es mayor que 3")

# <=     "    true "  "     "      "  " der  "   "   "   "    "   "  "  " izq
if 3 < 4:
  print("3 es menor que 4")

# != devuelve true si ambos operandos no son iguales
if 3 != 4:
  print("3 es diferente de 4")

#Estructuras repetitivas
#while
value = 1
while value <= 100: # la primera vez, value vale 1 -> true
                    # la segunda vez, value vale 51 -> true
                    # Value vale ahora 101 -> false
  value = value + 50
  print(value)

#for
for number in range(10): #range(n-1)
  print(number)