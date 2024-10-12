#los diccionarios se utilizan para estructuras mas complejas

#ejemplos de diccionarios de datos:
product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "name": "juan diego",
    "lastname": "jurado flores",
    "nickname": "jdiego.jurado"
}

#se obtienen los metodos que se pueden utilizar con un diccionario
print(dir(product))

#obtener todos los registros de un diccionario
print(person.items())

#obtener los keys (nombres de campos)
print(person.keys())

#limpiar todos los items
person.clear()

print(person)

#se pueden crear listas de diccionarios
#similar a entidades
products2 =[
    {"name":"book", "price": 10.99},
    {"name":"laptop", "price": 20.20}
]

print(products2)

#eliminar un diccionario
del person





