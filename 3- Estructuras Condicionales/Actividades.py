# Activdad 1
# Pedimos la edad al usuario y convertimos la entrada a número entero
edad = int(input("Ingrese su edad: "))

# Verificamos si la edad ingresada es mayor o igual a 18
if edad >= 18:
    # Si la condición se cumple, imprimimos que es mayor de edad
    print(f"Es mayor de edad")

# Actividad 2
# Pedimos al usuario que ingrese la nota de su examen
# Usamos int() para convertir la entrada en un número entero
nota = int(input("Ingrese la nota de su examen: "))

# Verificamos si la nota es mayor o igual a 6
if nota >= 6:
    # Si la condición se cumple, significa que aprobó
    print(f"Aprobado")
else:
    # Si la condición NO se cumple, significa que desaprobó
    print(f"Desaprobado")

# Actividad 3
# Pedimos al usuario que ingrese un número
# Usamos int() para asegurarnos de que el valor sea un número entero
numero = int(input("Ingrese un numero par: "))

# Verificamos si el número es par usando el operador módulo (%)
# Un número es par si al dividirlo por 2 el resto es 0
if numero % 2 == 0:
    # Si la condición se cumple, el número es par
    print(f"Ha ingresado un numero par")
else:
    # Si la condición no se cumple, significa que el número es impar
    print(f"Por favor, ingrese un numero par")


# Actividad 4
# Pedimos al usuario que ingrese su edad
# Convertimos la entrada a un número entero usando int()
edad = int(input("Ingrese su edad: "))

# Verificamos si la edad es mayor o igual a 30
if edad >= 30:
    # Si se cumple, el usuario es un adulto
    print(f"Eres adulto/a")

# Si no se cumple la primera condición, verificamos si la edad está entre 18 y 29
elif edad >= 18 and edad < 30:
    # Si se cumple, el usuario es un adulto joven
    print(f"Eres adulto/a joven")

# Si no se cumple ninguna de las anteriores, verificamos si la edad está entre 12 y 17
elif edad >= 12 and edad < 18:
    # Si se cumple, el usuario es adolescente
    print(f"Eres adolescente")

# Si ninguna de las condiciones anteriores se cumple, significa que es menor de 12
else:
    # El usuario es un niño o niña
    print(f"Eres niño/a")


# Actividad 5
# Pedimos al usuario que ingrese una contraseña
# Usamos str() para asegurarnos de que sea una cadena de texto
contraseña = str(input("Ingrese una contraseña: "))

# Verificamos si la longitud de la contraseña está entre 8 y 14 caracteres
if len(contraseña) >= 8 and len(contraseña) <= 14:
    # Si se cumple la condición, la contraseña es válida
    print(f"Ha ingresado una contraseña correcta")
else:
    # Si no se cumple la condición, la contraseña es demasiado corta o larga
    print(f"Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Actividad 6
# Importamos el módulo random para generar números aleatorios
import random
# Importamos las funciones mode, median y mean del módulo statistics
from statistics import mode, median, mean

# Creamos una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos la moda de la lista
mi_moda = mode(numeros_aleatorios)
# Calculamos la mediana de la lista
mi_mediana = median(numeros_aleatorios)
# Calculamos la media (promedio) de la lista
mi_media = mean(numeros_aleatorios)

# Mostramos la lista y los valores calculados
print("Lista de números:", numeros_aleatorios)
print("Media:", mi_media)
print("Mediana:", mi_mediana)
print("Moda:", mi_moda)

# Determinamos el tipo de sesgo de la distribución según los criterios dados
if mi_media > mi_mediana > mi_moda:
    # Sesgo positivo: la cola de la distribución está hacia la derecha
    resultado = "La distribución tiene sesgo positivo (a la derecha)."
elif mi_media < mi_mediana < mi_moda:
    # Sesgo negativo: la cola de la distribución está hacia la izquierda
    resultado = "La distribución tiene sesgo negativo (a la izquierda)."
elif mi_media == mi_mediana == mi_moda:
    # Sin sesgo: distribución simétrica
    resultado = "La distribución no presenta sesgo (simétrica)."
else:
    # Caso en que no se cumple exactamente ninguno de los criterios anteriores
    resultado = "No cumple exactamente con los criterios de sesgo definidos."

# Mostramos el resultado del análisis del sesgo
print(resultado)


# Actividad 7
# Pedimos al usuario que ingrese una palabra o frase
texto = input("Ingrese una palabra o frase: ")

# Definimos las vocales (mayúsculas y minúsculas) para la verificación
vocales = "aeiouAEIOU"

# Verificamos dos cosas:
# 1. Que el texto ingresado no esté vacío (len(texto) > 0)
# 2. Que el último carácter del texto sea una vocal (texto[-1] in vocales)
if len(texto) > 0 and texto[-1] in vocales:
    # Si se cumple, agregamos un signo de exclamación al final del texto
    texto += "!"

# Mostramos el resultado final
print(f"Resultado: {texto}")


# Actividad 8
# Pedimos al usuario que ingrese su nombre
nombre = str(input("Ingrese su nombre: "))

# Mostramos las opciones disponibles para transformar el nombre
print(f"Opciones:")
print(f"1. Nombre en MAYÚSCULAS")
print(f"2. Nombre en minúsculas")
print(f"3. Nombre con la primera letra en mayúscula")

# Pedimos al usuario que elija una opción (1, 2 o 3) y la convertimos a entero
opcion = int(input("Ingrese 1, 2 o 3 según la opción deseada: "))

# Evaluamos la opción elegida y transformamos el nombre según corresponda
if opcion == 1:
    # Opción 1: Convertir todo el nombre a mayúsculas
    resultado = nombre.upper()
elif opcion == 2:
    # Opción 2: Convertir todo el nombre a minúsculas
    resultado = nombre.lower()
elif opcion == 3:
    # Opción 3: Convertir la primera letra de cada palabra en mayúscula
    resultado = nombre.title()
else:
    # Si no es ninguna de las opciones válidas, mostramos un mensaje de error
    resultado = "Opción no válida."

# Mostramos el resultado final
print(f"Resultado {resultado}")


# Actividad 9
# Pedimos al usuario que ingrese la magnitud del terremoto en la escala de Richter
# Convertimos la entrada a número decimal (float) ya que puede tener decimales
magnitud = float(input("Ingrese en escala de Ritcher la magnitud de un terremoto: "))

# Evaluamos la magnitud para clasificar el terremoto según su intensidad
if magnitud < 3.0:
    # Magnitud menor a 3 → muy leve, imperceptible
    print(f"Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    # Magnitud entre 3 y 3.9 → leve, apenas perceptible
    print(f"Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    # Magnitud entre 4 y 4.9 → moderado, sentido por personas, daños mínimos
    print(f"Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    # Magnitud entre 5 y 5.9 → fuerte, puede dañar estructuras débiles
    print(f"Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    # Magnitud entre 6 y 6.9 → muy fuerte, daños significativos posibles
    print(f"Muy fuerte (puede causar daños significativos)")
else:
    # Magnitud 7 o mayor → extremo, daños a gran escala
    print(f"Extremo (puede causar daños a gran escala)")


# Actividad 10
# Pedimos al usuario que ingrese su hemisferio (N para norte / S para sur)
# .strip() elimina espacios en blanco al inicio o final, .upper() convierte a mayúscula
hemisferio = input("Ingrese su hemisferio (N para norte / S para sur): ").strip().upper()

# Pedimos el mes como número entero (1-12)
mes = int(input("Ingrese el mes (1-12): "))

# Pedimos el día como número entero (1-31)
dia = int(input("Ingrese el día (1-31): "))

# Determinamos la estación según el hemisferio y la fecha ingresada
if hemisferio == "N":
    # Hemisferio Norte
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        # Entre 21 de diciembre y 20 de marzo → Invierno
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        # Entre 21 de marzo y 20 de junio → Primavera
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        # Entre 21 de junio y 20 de septiembre → Verano
        estacion = "Verano"
    else:
        # Entre 21 de septiembre y 20 de diciembre → Otoño
        estacion = "Otoño"

elif hemisferio == "S":
    # Hemisferio Sur
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        # Entre 21 de diciembre y 20 de marzo → Verano
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        # Entre 21 de marzo y 20 de junio → Otoño
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        # Entre 21 de junio y 20 de septiembre → Invierno
        estacion = "Invierno"
    else:
        # Entre 21 de septiembre y 20 de diciembre → Primavera
        estacion = "Primavera"
else:
    # Si el hemisferio ingresado no es N ni S
    estacion = "Hemisferio no válido."

# Mostramos la estación correspondiente
print(f"En el hemisferio {hemisferio}, el {dia}/{mes} corresponde a {estacion}.")
