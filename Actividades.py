#Actividad 1
print("Hola Mundo!")

#Actividad 2
<<<<<<< Updated upstream
##Pedimos al usuario ingresar su nombre
nombre = input("Como te llamas?: ")
##Mostramos el nombre ingresado en pantalla
print(f"Hola {nombre}!")

#Actividad 3
##Pedimos al usuario que ingrese su nombre, apellido, edad y lugar de residencia.
=======
nombre = input("Como te llamas?: ")
print(f"Hola {nombre}!")

#Actividad 3
>>>>>>> Stashed changes
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
lugarderesidencia = input("Lugar de Residencia: ")
<<<<<<< Updated upstream
##Mostramos los datos ingresados por el usuario
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarderesidencia}")

#Actividad 4
##Pedimos al usuario que ingrese un radio para un circulo
radio = int(input("Ingrese el radio del circulo: "))
##Hacemos el calculo entre el radio del circulo ingresado para sacar el area y el perimetro
area = 3.14 * radio**2
perimetro = 2 * 3.14 * radio
##Mostramos en pantalla el area y el perimetro del circulo
=======
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarderesidencia}")

#Actividad 4
radio = int(input("Ingrese el radio del circulo: "))
area = 3.14 * radio**2
perimetro = 2 * 3.14 * radio
>>>>>>> Stashed changes
print(f"El area del circulo es de: {area}")
print(f"El perimetro del circulo es de: {perimetro}")

#Actividad 5
<<<<<<< Updated upstream
##Pedimos al usuario que ingrese una x cantidad de segundos
segundos = int(input("Ingrese una cantidad de segundos: "))
##Pasamos los segundos ingresados a horas
hora = segundos / 3600
##Mostramos cuantas horas son el total los segundos ingresados anteriormente.
print(f"{segundos} segundos son {hora} horas")

#Actividad 6
##Le pedimos al usuario que ingrese un numero
numero = int(input("Ingrese un numero: "))
#Mostramos en pantalla la tabla del 1 al 10 del numero ingresado
=======
segundos = int(input("Ingrese una cantidad de segundos: "))
hora = segundos / 3600
print(f"{segundos} segundos son {hora} horas")

#Actividad 6
numero = int(input("Ingrese un numero: "))
>>>>>>> Stashed changes
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#Actividad 7
<<<<<<< Updated upstream
##Le pedimos al usuario que ingrese dos numeros enteros mayores a 0
numeroA = int(input("Ingrese un numero entero mayor a 0: "))
numeroB = int(input("Ingrese otro numero entero mayor a 0: "))
##Realizamos la suma, resta, multiplicacion y division de los dos numeros ingresados.
=======
numeroA = int(input("Ingrese un numero entero mayor a 0: "))
numeroB = int(input("Ingrese otro numero entero mayor a 0: "))
>>>>>>> Stashed changes
suma = numeroA + numeroB
resta = numeroA - numeroB
multiplicacion = numeroA * numeroB
division = numeroA / numeroB
<<<<<<< Updated upstream
#Mostramos en pantalla el resultado de los calculos
=======
>>>>>>> Stashed changes
print(f"{numeroA} + {numeroB} = {suma}")
print(f"{numeroA} - {numeroB} = {resta}")
print(f"{numeroA} x {numeroB} = {multiplicacion}")
print(f"{numeroA} / {numeroB} = {division}")

#Actividad 8
<<<<<<< Updated upstream
##Pedimos al usuario que ingrese su altura y peso.
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
##Sacamos el IMC del usuario
IMC = peso / (altura**2)
##Mostramos en pantallas el IMC del usuario
print(f"Tu indice de masa corporal es de {IMC}")

#Actividad 9
##Pedimos al usuario que ingrese cuantos grados hacen actualmente usando Celcius
gradosCelcius = int(input("Ingrese cuantos grados hacen: "))
##Hacemos un calculo para pasar de grados Celcius a Fahrenheit
gradosfahrenheit = 9 / 5 * gradosCelcius + 32
##Mostramos el equivalente de los grados celcius a grados Fahrenheit
print(f"El equivalente de {gradosCelcius} grados celcius en grados fahrenheit es de {gradosfahrenheit}")

#Actividad 10
##Pedimos al usuario que ingrese tres numeros enteros
numeroA = int(input("Ingrese un numero entero: "))
numeroB = int(input("Ingrese un segundo numero entero: "))
numeroC = int(input("Ingrese un tercer numero entero: "))
##Hacemos dos calculos, donde sumamos los tres numeros pedidos para luego sacar el promedio total
suma = numeroA + numeroB + numeroC
promedio = suma / 3
##Mostramos el promedio entre los tres numeros ingresados.  
=======
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
IMC = peso / (altura**2)
print(f"Tu indice de masa corporal es de {IMC}")

#Actividad 9
gradosCelcius = int(input("Ingrese cuantos grados hacen: "))
gradosfahrenheit = 9 / 5 * gradosCelcius + 32
print(f"El equivalente de {gradosCelcius} grados celcius en grados fahrenheit es de {gradosfahrenheit}")

#Actividad 10
numeroA = int(input("Ingrese un numero entero: "))
numeroB = int(input("Ingrese un segundo numero entero: "))
numeroC = int(input("Ingrese un tercer numero entero: "))
suma = numeroA + numeroB + numeroC
promedio = suma / 3
>>>>>>> Stashed changes
print(f"El promedio entre {numeroA}, {numeroB} y {numeroC} es {promedio}")