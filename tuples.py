#se utiliza para principio de inmutabilidad
#son mas rapidas
#codigo mas seguro
#no pueden variar sus valores
#utilizar para valores constantes

#declaracion de una tupla
x = (1, 2, 3)
print(x)
print(type(x))

#otra forma de declaracion
x = tuple((1, 2, 3))
print(x)
print(type(x))

#obtener los metodos que se pueden utilizar en una tupla
print(dir(tuple()))

#ejemplos:
x = (1, 2, 3, 4, 5)

#obtener un valor de una tupla por el indice
print(x[0])

#ejemplo de un diccionario, que contiene tuplas
location = {
    (35.13, 39.00): "Tokio",
    (48.30, 45.22): "New York"
}

print(location)
print(type(location))

#para eliminar una tupla
del x


