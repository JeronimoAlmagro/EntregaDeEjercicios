##Ejercicio 1
# Diccionario con los precios de algunas frutas
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
}

# Agrega "Naranja" al diccionario usando get para asignar un valor por defecto
# Si "Maranja" no existe, asigna 1200
precios_frutas["Naranja"] = precios_frutas.get("Maranja", 1200) 

# Agrega "Manzana" al diccionario con valor por defecto 1500
precios_frutas["Manzana"] = precios_frutas.get("Manzana", 1500)

# Agrega "Pera" al diccionario con valor por defecto 2300
precios_frutas["Pera"] = precios_frutas.get("Pera", 2300)

# Muestra el diccionario actualizado
print(precios_frutas)


##Ejercicio 2
# Diccionario con los precios de varias frutas
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualiza el precio de la Banana
precios_frutas['Banana'] = 1330

# Actualiza el precio de la Manzana
precios_frutas['Manzana'] = 1700

# Actualiza el precio del Melon
precios_frutas['Melón'] = 2800

# Muestra el diccionario con los precios actualizados
print(precios_frutas)


##Ejercicio 3
# Diccionario con los precios de varias frutas
precios_frutas = {
    'Banana': 1330, 
    'Ananá': 2500, 
    'Melón': 2800, 
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Muestra solo las claves del diccionario (nombres de las frutas)
print(precios_frutas.keys())


##Ejercicio 4
# Diccionario vacio para almacenar los contactos
contactos = {

}

# Bucle para ingresar 5 contactos
for i in range(5):
    # Solicita el nombre del contacto
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    # Solicita el numero del contacto
    numero = input(f"Ingrese el número de {nombre}: ")
    # Agrega el contacto al diccionario
    contactos[nombre] = numero

# Solicita el nombre del contacto a buscar
buscar = input("Ingrese el nombre del contacto a buscar: ")

# Verifica si el contacto existe en el diccionario
if buscar in contactos:
    # Muestra el numero del contacto
    print(f"El número de {buscar} es: {contactos[buscar]}")
else:
    # Mensaje si el contacto no existe
    print("Ese contacto no existe en la agenda.")


##Ejercicio 5
# Solicita al usuario ingresar una frase
frase = input("Ingrese una frase: ")

# Separa la frase en palabras usando espacio como separador
palabras = frase.split()

# Crea un conjunto con las palabras unicas
palabras_unicas = set(palabras)

# Diccionario vacio para almacenar el recuento de cada palabra
recuento = {

}

# Bucle para contar cuantas veces aparece cada palabra
for palabra in palabras:
    if palabra in recuento:
        # Si la palabra ya esta en el diccionario, suma 1
        recuento[palabra] += 1
    else:
        # Si la palabra no esta, la agrega con valor 1
        recuento[palabra] = 1

# Muestra las palabras unicas
print("Palabras únicas:", palabras_unicas)
# Muestra el recuento de todas las palabras
print("Recuento:", recuento)


##Ejercicio 6
# Diccionario vacio para almacenar los alumnos y sus notas
alumnos = {

}

# Bucle para ingresar datos de 3 alumnos
for i in range(3):
    # Solicita el nombre del alumno
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    # Solicita las tres notas del alumno
    nota1 = int(input("Ingrese la primera nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercera nota: "))
    # Agrega el alumno y sus notas como una tupla al diccionario
    alumnos[nombre] = (nota1, nota2, nota3)

# Muestra los promedios de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    # Calcula el promedio sumando las notas y dividiendo por la cantidad
    promedio = sum(notas) / len(notas)
    # Muestra el nombre del alumno y su promedio con 2 decimales
    print(f"{nombre}: {promedio:.2f}")


##Ejercicio 7
# Diccionario con los alumnos que aprobaron cada parcial
aprobados = {
    "Parcial 1": {"Ana", "Luis", "Sofía", "Juan"},
    "Parcial 2": {"Sofía", "Pedro", "Juan", "Carla"}
}

# Conjuntos con los alumnos que aprobaron cada parcial
parcial1 = aprobados["Parcial 1"]
parcial2 = aprobados["Parcial 2"]

# Alumnos que aprobaron ambos parciales (interseccion)
ambos = parcial1 & parcial2

# Alumnos que aprobaron solo uno de los dos parciales (simetrica diferencia)
solo_uno = parcial1 ^ parcial2

# Alumnos que aprobaron al menos un parcial (union)
al_menos_uno = parcial1 | parcial2

# Muestra los resultados
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)


##Ejercicio 8
# Diccionario con el stock inicial de algunos productos
stock = {
    "Manzana": 10,
    "Banana": 5,
    "Pera": 8
}

# Muestra el stock actual
print("Stock actual:", stock)

# Solicita el nombre del producto a consultar
producto = input("Ingrese el nombre del producto a consultar: ")

# Verifica si el producto existe en el diccionario
if producto in stock:
    # Muestra el stock actual del producto
    print(f"El stock de {producto} es: {stock[producto]} unidades.")
    # Solicita cuantas unidades desea agregar
    agregar = int(input("¿Cuántas unidades desea agregar? "))
    # Actualiza el stock del producto
    stock[producto] += agregar
    print(f"Ahora el stock de {producto} es: {stock[producto]} unidades.")
else:
    # Si el producto no existe, solicita el stock inicial
    print(f"El producto '{producto}' no existe en el stock.")
    nuevo = int(input("Ingrese el stock inicial de este nuevo producto: "))
    # Agrega el nuevo producto al diccionario
    stock[producto] = nuevo
    print(f"Se agregó '{producto}' con {nuevo} unidades.")

# Muestra el stock actualizado
print("Stock actualizado:", stock)


##Ejercicio 9
# Diccionario que representa la agenda con claves como tuplas (dia, hora)
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Gimnasio"
}

# Muestra los eventos actuales de la agenda
print("Agenda actual:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

# Solicita al usuario un dia y una hora para consultar
dia = input("\nIngrese un día: ")
hora = input("Ingrese una hora (HH:MM): ")

# Verifica si hay un evento en la fecha y hora indicada
if (dia, hora) in agenda:
    print(f"Evento: {agenda[(dia, hora)]}")
else:
    # Si no hay evento, pregunta si desea agregar uno
    print("No hay evento en ese día y hora.")
    nuevo_evento = input("¿Desea agregar un evento? (s/n): ")
    if nuevo_evento.lower() == "s":
        # Solicita el nombre del evento y lo agrega a la agenda
        evento = input("Ingrese el nombre del evento: ")
        agenda[(dia, hora)] = evento
        print("Evento agregado correctamente.")

# Muestra la agenda actualizada con los cambios realizados
print("\nAgenda actualizada:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")


##Ejercicio 10
# Diccionario original con paises como claves y sus capitales como valores
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}

# Crea un nuevo diccionario invirtiendo claves y valores
invertido = {valor: clave for clave, valor in original.items()}

# Muestra el diccionario invertido
print(invertido)
