#se declara sin un indice:
#se utiliza para que se tenga un listado simple sin un orden especifico

colors = {"red", "blue", "yellow"}
print(type(colors))

#para saber que metodos se pueden utilizar con SET
print(dir(colors))

#añadir un elemento al set
colors.add("violet")
print(colors)

#eliminar un elemento del set
colors.remove("red")
print(colors)

#verificar si existe un elemento en el set
print(("yellow" in colors))

#limpiar todos los datos
colors.clear()
print(colors)

#eliminar totalmente un set
del colors


