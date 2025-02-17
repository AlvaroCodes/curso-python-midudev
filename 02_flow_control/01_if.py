###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
#
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# num1 = int(input("Introduce el primer número: "))
# num2 = int(input("Introduce el segundo número: "))
# if num1 > num2:
#  print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#  print(f"{num2} es mayor que {num1}")
# else:
#  print(f"{num1} y {num2} son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# num1 = int(input("Introduce el primer número: "))
# num2 = int(input("Introduce el segundo número: "))
# operador = input("Introduce Operador: ")

# if operador == '+':
#  print(f"{num1 + num2}")
# elif operador == '-':
#  print(f"{num1 - num2}")
# elif operador == '*':
#  print(f"{num1 * num2}")
# elif operador == '/' and num1 != 0 and num2 != 0:
#  print(f"{num1 / num2}")
# else:
#  print("No se puede dividir por 0") 

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# anio = int(input("Introduce un año: "))
# if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#     print(f"{anio} es un año bisiesto.")
# else:
#     print(f"{anio} no es un año bisiesto.")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# edad = int(input("Introduce edad: "))
# if (edad >= 0 and edad <= 2):
#  print("Bebé")
# elif (edad >= 3 and edad <= 12):
#  print("Niño")
# elif (edad >= 13 and edad <= 17):
#  print("Adolescente")
# elif (edad >= 18 and edad <= 64):
#  print("Adulto")
# elif (edad >= 65):
#  print("Adulto mayor")