##Ejercicio 1
# Lista de múltiplos de 4 entre 1 y 100
multiplos_de_4 = list(range(4, 101, 4))
# Mostrar lista
print(multiplos_de_4)


##Ejercicio 2
# Creamos una lista con los numeros del 1 al 5
lista = [1, 2, 3, 4, 5]

# Accedemos al penultimo elemento usando indice negativo (-2)
penultimo_elemento = lista[-2]

# Imprimimos el penultimo elemento
print(penultimo_elemento)


##Ejercicio 3
# Creamos una lista vacia
lista = []

# Recorremos un rango de 3 posiciones (0, 1, 2)
for i in range(3):
    # Pedimos al usuario que ingrese una palabra para la posicion correspondiente
    palabra_a_agregar = str(input(f"Ingrese una palabra para la posicion {i}: "))
    
    # Agregamos la palabra ingresada a la lista
    lista.append(palabra_a_agregar)

# Mostramos la lista completa por pantalla
print(lista)



##Ejercicio 4
# Creamos una lista con algunos animales
lista_animales = ['perro','gato','conejo','pez']

# Mostramos la lista original
print(lista_animales)

# Pedimos al usuario que ingrese un nuevo animal para reemplazar al segundo elemento (indice 1)
lista_animales[1] = str(input(f"Ingrese un numevo animal para reemplazar a {lista_animales[1]}: "))

# Pedimos al usuario que ingrese un nuevo animal para reemplazar al cuarto elemento (indice 3)
lista_animales[3] = str(input(f"Ingrese un nuevo animal para reemplazar a {lista_animales[3]}: "))

# Mostramos la lista actualizada
print(lista_animales)


##Ejercicio 5
#Lo que realiza el programa es eliminar el valor mas alto de la lista con la funcion max(), en este caso el 22.


##Ejercicio 6
# Creamos una lista con numeros del 10 al 30, haciendo saltos de 5 en 5
lista = list(range(10, 31, 5))

# Mostramos la lista completa
print("Lista completa:", lista)

# Mostramos los dos primeros elementos de la lista usando slicing
print("Dos primeros:", lista[:2])


##Ejercicio 7
# Creamos una lista con algunos autos
autos = ['sedan', 'polo', 'suran', 'gol']

# Mostramos la lista original
print(autos)

# Pedimos al usuario que ingrese un nuevo elemento para reemplazar el segundo auto (indice 1)
autos[1] = str(input(f"Ingrese un nuevo elementos para reemplazar {autos[1]} por lo que quieras: "))

# Pedimos al usuario que ingrese un nuevo elemento para reemplazar el tercer auto (indice 2)
autos[2] = str(input(f"Ingrese un nuevo elementos para reemplazar {autos[2]} por lo que quieras: "))

# Mostramos la lista actualizada
print(autos)


##Ejercicio 8
# Creamos una lista vacia
dobles = []

# Agregamos el doble de 5 a la lista
dobles.append(5 * 2)

# Agregamos el doble de 10 a la lista
dobles.append(10 * 2)

# Agregamos el doble de 15 a la lista
dobles.append(15 * 2)

# Mostramos la lista con los valores agregados
print(dobles)


##Ejercicio 9
# Creamos una lista de listas con los productos comprados por distintos clientes
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

# Agregamos 'jugo' a la lista del tercer cliente (indice 2)
compras[2].append('jugo')

# Reemplazamos 'fideos' por 'tallarines' en la lista del segundo cliente (indice 1, posicion 1)
compras[1][1] = 'tallarines'

# Eliminamos 'pan' de la lista del primer cliente (indice 0)
compras[0].remove('pan')

# Mostramos la lista actualizada
print(compras)


#Ejercicio 10
# Creamos una lista anidada con distintos tipos de elementos
lista_anidada = [
    15,                  # posicion [0]
    True,                # posicion [1]
    [25.5, 57.9, 30.6],  # posicion [2] que es otra lista con 3 elementos
    False                # posicion [3]
]

# Mostramos la lista anidada completa
print(lista_anidada)