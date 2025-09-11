##Ejercicio 1
# Imprimir números del 0 al 100
for numero in range(0, 101):
    print(numero)


## Ejercicio 2
# Solicita al usuario un numero entero
numero = int(input("Ingresa un numero entero: "))

# Convierte el numero a positivo en caso de ser negativo
numero_abs = abs(numero)

# Convierte el numero a cadena y cuenta los caracteres
cantidad_digitos = len(str(numero_abs))

# Muestra el resultado
print(f"El numero tiene {cantidad_digitos} digito(s).")


## Ejercicio 3
# Solicita al usuario dos números enteros
inicio = int(input("Ingresa el primer numero entero: "))
fin = int(input("Ingresa el segundo numero entero: "))

# Calcula la suma de los numeros entre los dos valores, excluyendolos
suma = sum(range(inicio + 1, fin))

# Muestra el resultado
print(f"La suma de los numeros entre {inicio} y {fin} (excluyendolos) es: {suma}")


## Ejercicio 4
# Inicializar la variable de suma acumulada
suma_total = 0

# Bucle para solicitar núueros hasta que el usuario ingrese un 0
while True:
    numero = int(input("Ingresa un numero entero (ingresa 0 para finalizar): "))
    
    # Si el numero es 0, se sale del bucle
    if numero == 0:
        break
    
    # Sumar el numero al total acumulado
    suma_total += numero

# Mostrar el total acumulado
print(f"La suma total de los numeros ingresados es: {suma_total}")


## Ejercicio 5
import random

# Generar un numero aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

# Inicializar el contador de intentos
intentos = 0

# Bucle para que el usuario siga adivinando
while True:
    # Solicitar al usuario que ingrese un numero
    adivinanza = int(input("Adivina el numero entre 0 y 9: "))
    
    # Incrementar el contador de intentos
    intentos += 1
    
    # Comprobar si el numero ingresado es el correcto
    if adivinanza == numero_aleatorio:
        print(f"Felicidades! Has acertado el numero en {intentos} intento(s).")
        break
    elif adivinanza < numero_aleatorio:
        print("El numero es mayor. Intenta de nuevo.")
    else:
        print("El numero es menor. Intenta de nuevo.")


## Ejercicio 6
# Imprimir numeros pares entre 0 y 100 en orden decreciente
for numero in range(100, -1, -2):
    print(numero)


## Ejercicio 7
# Solicitar al usuario un numero entero positivo
numero = int(input("Ingresa un numero entero positivo: "))

# Verificar que el numero ingresado sea positivo
if numero < 0:
    print("Por favor, ingresa un numero entero positivo.")
else:
    # Calcular la suma de los numeros desde 0 hasta el numero ingresado
    suma = sum(range(numero + 1))

    # Mostrar el resultado
    print(f"La suma de los numeros desde 0 hasta {numero} es: {suma}")


## Ejercicio 8
# Inicializar contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Numero de entradas que el usuario debe proporcionar
cantidad_numeros = 100

# Solicitar al usuario que ingrese los numeros
for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el numero {i + 1}: "))
    
    # Verificar si el numero es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Verificar si el numero es positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostrar los resultados
print(f"Resultados después de ingresar {cantidad_numeros} numeros:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")


## Ejercicio 9
# Inicializar la suma total
suma_total = 0

# Numero de entradas que el usuario debe proporcionar
cantidad_numeros = 100

# Solicitar al usuario que ingrese los numeros
for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el numero {i + 1}: "))
    
    # Acumular la suma total
    suma_total += numero

# Calcular la media
media = suma_total / cantidad_numeros

# Mostrar el resultado
print(f"La media de los {cantidad_numeros} numeros ingresados es: {media}")


## Ejercicio 10
# Solicitar al usuario un numero entero
numero = input("Ingresa un numero entero: ")

# Invertir el orden de los digitos usando slicing
numero_invertido = numero[::-1]

# Mostrar el numero invertido
print(f"El numero invertido es: {numero_invertido}")