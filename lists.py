#Lista de valores con distintos tipos de datos
[1, "hola", 1.5, True, [1, 2, 3]]

#Lista de colores
colors = ["azul", "amarillo", "rojo"]
#Impresion de la lista de colores en pantalla
print(colors)

#Lista de numeros
number_list = list((1, 2, 3, 4))
#Se muestra la lista de numeros
print(number_list)
#Se obtiene el tipo de dato de lista
print(type(number_list))


#range:
#Listado de valores en lista utilizando el comando range(rango)
range(1, 10)
print(range(1, 1000))

#Otra manera de ejecutar range
rango_numeros = list(range(1, 11))
print(rango_numeros)
print(type(rango_numeros))


#Qué metodos se pueden utilizar en las listas?
print(dir(list()))

#Conocer la longitu de una lista
print(len(rango_numeros))

#devolver el valor en una posicion de una lista
print(colors[0])
print(colors[1])
print(colors[-1]) #indice inverso

#buscar un elemento especifico en una lista
print('xxx' in colors) #si no existe devuelve foalse, si existe devuelve true.
print('azul' in colors)

#cambiar el valor de un elemento de la lista
print(colors)
colors[0] = "violeta"
print(colors)

#añadir un color a la lista de colores
print(colors)
colors.append("negro")
print(colors)

#añadir varios elementos con un solo comando
#se usa el comando extend, y se manda como parameatro una lista
colors.extend(("naranja", "blanco"))
print(colors)

#añadir un elemento en una posicion especifica
colors.insert(1, 'marron')
print(colors)

#añadir un elemento al final de la lista
colors.insert(len(colors), 'turquesa')
print(colors)

#eliminar el ultimo elemento de una lista
colors.pop()
print(colors)

#eliminar un elemento especifico utilizando el indice
colors.pop(1)
print(colors)

#eliminar un elemento basado en el valor
colors.remove("amarillo")
print(colors)

#ordenar todos los elementos de una lista
#alfabeticamente
colors.sort()
print(colors)

#alfabetica inversa
colors.sort(reverse=True)
print(colors)

#buscar el indice de un elemento por su valor
print(colors.index('naranja'))

#contar las veces en las que aparece un elemento
print(colors.count('negro'))

#eliminar todos los elementos de una lista
colors.clear()
print(colors)




