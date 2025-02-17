###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
#
#  EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
num_1 = 1
while num_1 <= 10:
  print(num_1)
  num_1 += 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
num_2 = 1
peers = 0
while num_2 <= 20:
  if (num_2 % 2 == 0):
    peers+= num_2
  num_2 += 1
print(peers)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
num_3 = int(input("Introduce un número entero positivo: "))
fact = 1
counter = 1

while counter <= num_3:
  fact *= counter
  counter += 1

print(fact)

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

pass_user = ''
while len(pass_user) < 8:
  pass_user = input('Introduce la contraseña: ')

  if (len(pass_user) < 8):
    print('Introduce de nuevo la contraseña, +8 caracteres')

print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

num_5 = 1
num_user_5 = int(input('Introduce un numero: '))

while num_5 <= 10:
  print(f"{num_user_5} x {num_5} = {num_user_5 * num_5}")
  num_5 += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
num_6_user = int(input("Introduzca un número entero positivo:"))
num_6 = 2
while num_6 <= num_6_user:
  is_prime = True 
  div = 2
  while div * div <= num_6:
    if num_6 % div == 0:
      is_prime = False
      break  
    div += 1
  if is_prime:
    print(num_6)

  num_6 += 1
