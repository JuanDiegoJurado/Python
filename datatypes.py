#Obtener el tipo de valor de una variable
print(type("Hola"))

#entero
print(type(1))

#string
print(type('Hola mundo'))
print(type('''Hola mundo'''))

#float
print(type(1.60))

#Python tiene tipado dinámico.
#Lo que quiere decir que una variable puede cambiar de tipo de dato fácilmente

#Union de 2 strings:
print("Bye" + "World")

#booleano
print(type(False))
print(type(True))

#listas (son de capacidad variable)
print(type([10, 20, 30, 40]))
print(type(["Hello", "Bye", "Adios"]))
print(type(["HOLA", 1, False, 1.5]))
#Lista vacía
[]

print([10, 20, 30])

#tuplas (de capacidad especifica. No se puede modificar. Principio de )
print((1, 2, 3))

print(type((1, 2)))
#tupla vacía
()

#diccionarios
#Permite agrupar datos en una misma entidad
print(
{
    "name": "Juan Diego",   
    "lastname": "Jurado Flores",
    "age": 36,
    "sex": "M"
}
)

print(type(
{
    "name": "Juan Diego",   
    "lastname": "Jurado Flores",
    "age": 36,
    "sex": "M"
}))

#set
print(type(
{
 "Juan Diego",   
 "Jurado",
 "Flores"
}))


#Tipo de dato NONE indica que no tiene definido un tipo de dato
None
print(type(None))

