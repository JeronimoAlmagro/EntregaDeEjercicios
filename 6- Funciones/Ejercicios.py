##Ejercicio 1
# Definimos una funcion llamada imprimir_hola_mundo
def imprimir_hola_mundo():
    # Usamos return junto con print para mostrar el mensaje "Hola Mundo!"
    return print("Hola Mundo!")

# Llamamos a la funcion
imprimir_hola_mundo()


##Ejercicio 2
# Definimos una funcion que recibe un nombre como parametro
def saludar_usuario(nombre):
    # Usamos return junto con print para mostrar un saludo personalizado
    return print(f"Hola {nombre}!")

# Pedimos al usuario que ingrese su nombre
nombre = str(input("Ingrese su nombre: "))

# Llamamos a la funcion pasando como argumento el nombre ingresado
saludar_usuario(nombre)


##Ejercicio 3
# Definimos una funcion que recibe cuatro parametros: nombre, apellido, edad y residencia
def informacion_personal(nombre,apellido,edad,residencia):
    # Usamos return junto con print para mostrar la informacion personal
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# Pedimos al usuario que ingrese su nombre
nombre = str(input("Ingrese su nombre: "))

# Pedimos al usuario que ingrese su apellido
apellido = str(input("Ingrese su apellido: "))

# Pedimos al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Pedimos al usuario que ingrese su lugar de residencia
residencia = str(input("Ingrese su residencia: "))

# Llamamos a la funcion pasando como argumentos los datos ingresados
informacion_personal(nombre,apellido,edad,residencia)


##Ejercicio 4
# Importamos la libreria math para usar el valor de pi
import math  

# Definimos una funcion que calcula el area de un circulo dado su radio
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

# Definimos una funcion que calcula el perimetro de un circulo dado su radio
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Pedimos al usuario que ingrese el radio del circulo
radio = float(input("Ingrese el radio del circulo: "))

# Mostramos el resultado del area llamando a la funcion
print("El area del circulo es:", calcular_area_circulo(radio))

# Mostramos el resultado del perimetro llamando a la funcion
print("El perimetro del circulo es:", calcular_perimetro_circulo(radio))


##Ejercicio 5
# Definimos una funcion que convierte segundos a horas
def segundos_a_horas(segundos):
    # Dividimos los segundos entre 3600 (cantidad de segundos que tiene una hora)
    return segundos / 3600

# Pedimos al usuario que ingrese la cantidad de segundos
segundos = float(input("Ingrese los segundos que desee: "))

# Mostramos el resultado llamando a la funcion
print("Equivalente en horas:", segundos_a_horas(segundos))


##Ejercicio 6
# Definimos una funcion que imprime la tabla de multiplicar de un numero
def tabla_multiplicar(numero):
    # Recorremos los numeros del 1 al 10
    for i in range(1, 11):
        # Mostramos la multiplicacion en cada iteracion
        print(f"{numero} x {i} = {numero * i}")

# Pedimos al usuario que ingrese un numero
numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

# Llamamos a la funcion pasando como argumento el numero ingresado
tabla_multiplicar(numero)


##Ejercicio 7
# Definimos una funcion que realiza operaciones basicas entre dos numeros
def operaciones_basicas(a, b):
    suma = a + b                # Calculamos la suma
    resta = a - b               # Calculamos la resta
    multiplicacion = a * b      # Calculamos la multiplicacion
    division = a / b            # Calculamos la division
    # Devolvemos los resultados como una tupla
    return (suma, resta, multiplicacion, division)

# Pedimos al usuario que ingrese el primer numero
x = float(input("Ingrese el primer numero: "))

# Pedimos al usuario que ingrese el segundo numero
y = float(input("Ingrese el segundo numero: "))

# Llamamos a la funcion y guardamos los resultados en una tupla
resultados = operaciones_basicas(x, y)

# Mostramos los resultados de forma clara
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")


##Ejercicio 8
# Definimos una funcion que calcula el indice de masa corporal (IMC)
def calcular_imc(peso, altura):
    # Calculamos el IMC dividiendo el peso entre la altura al cuadrado
    IMC = peso / (altura ** 2)
    return(IMC)

# Pedimos al usuario que ingrese su peso en kilogramos
peso = float(input("Ingrese su peso en kg: "))

# Pedimos al usuario que ingrese su altura en metros
altura = float(input("Ingrese su altura en metros: "))

# Mostramos el IMC llamando a la funcion con los datos ingresados
print(f"Su indice de masa corporal es de {calcular_imc(peso,altura)}")


##Ejercicio 9
# Definimos una funcion que convierte de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    # Aplicamos la formula para convertir a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return(fahrenheit)

# Pedimos al usuario que ingrese la temperatura en Celsius
celsius = float(input("Ingrese la temperatura en Celcius: "))

# Mostramos la temperatura convertida llamando a la funcion
print(f"La temperatura en Fahrenheit es de {celsius_a_fahrenheit(celsius)}°F")


##Ejercicio 10
# Definimos una funcion que calcula el promedio de tres notas
def calcular_promedio(a,b,c):
    # Sumamos las tres notas
    suma_de_notas = a + b + c
    # Calculamos el promedio dividiendo la suma entre 3
    promedio = suma_de_notas / 3
    return(promedio)

# Pedimos al usuario que ingrese la primera nota
a = float(input("Ingrese la primera nota: "))

# Pedimos al usuario que ingrese la segunda nota
b = float(input("Ingrese la segunda nota: "))

# Pedimos al usuario que ingrese la tercera nota
c = float(input("Ingrese la tercera nota: "))

# Mostramos el promedio llamando a la funcion con las notas ingresadas
print(f"El promedio de las notas es de {calcular_promedio(a,b,c)}")
