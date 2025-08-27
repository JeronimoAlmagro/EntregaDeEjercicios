#Actividad 1
print("Hola Mundo!")

#Actividad 2
nombre = input("Como te llamas?: ")
print(f"Hola {nombre}!")

#Actividad 3
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
lugarderesidencia = input("Lugar de Residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarderesidencia}")

#Actividad 4
radio = int(input("Ingrese el radio del circulo: "))
area = 3.14 * radio**2
perimetro = 2 * 3.14 * radio
print(f"El area del circulo es de: {area}")
print(f"El perimetro del circulo es de: {perimetro}")

#Actividad 5
segundos = int(input("Ingrese una cantidad de segundos: "))
hora = segundos / 3600
print(f"{segundos} segundos son {hora} horas")

#Actividad 6
numero = int(input("Ingrese un numero: "))
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
numeroA = int(input("Ingrese un numero entero mayor a 0: "))
numeroB = int(input("Ingrese otro numero entero mayor a 0: "))
suma = numeroA + numeroB
resta = numeroA - numeroB
multiplicacion = numeroA * numeroB
division = numeroA / numeroB
print(f"{numeroA} + {numeroB} = {suma}")
print(f"{numeroA} - {numeroB} = {resta}")
print(f"{numeroA} x {numeroB} = {multiplicacion}")
print(f"{numeroA} / {numeroB} = {division}")

#Actividad 8
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
print(f"El promedio entre {numeroA}, {numeroB} y {numeroC} es {promedio}")