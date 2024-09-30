myStr = "Hello World"

#obtener los metodos que se pueden utilizar para el tipo de dato
print(dir(myStr))

#Texto en mayusculas
myStr = myStr.upper()
print(myStr)

#Metodos para mostrar un titulo
print(myStr.title())

#Metodo para convertirlo a minusculas
print(myStr.lower())

#Cambia mayusculas por minusculas
print(myStr.swapcase())

#Cambia mayusculas la primera letra
print(myStr.capitalize())

#Reemplaza la palabra world por Mundo
print(myStr.upper().replace("WORLD", "Mundo"))

#Contar numero de veces que aparece una letra
print(myStr.count("L"))

#verificar si un texto empieza con:
print(myStr.upper().startswith("HELLO"))

#verificar si un texto termina con:
print(myStr.upper().endswith("MUNDO"))
print(myStr.upper().endswith("WORLD"))

#convertir una cadena en una lista con split
print(myStr.split(" "))

#obtener la posicion en la que se encuentra una letra dentro de una cadena
print(myStr.find('o'))
print(myStr.find('O'))

#longitud de una cadena
print(len(myStr))

#posicion (indice) de una letra dentro de la cadena
print(myStr.index('W'))

#verificar si una cadena es numerica
print(myStr.isnumeric())
print(myStr.isalpha())

#obtener una posicion de una cadena
print(myStr[1]) 
print(myStr[-1]) #se obtienen las letras de manera inversa
print(myStr[-5]) #se obtienen las letras de manera inversa


#Para reemplazo de variables
nombre = "Juan Diego"
print("Mi nombre es: " + nombre)
print(f"Mi nombre es: {nombre}")
print("Mi nombre es: {0}".format(nombre))





#comentar todo con combinacion de teclas
# Se selecciona todo
# Luego se presiona CTRL + K 
# y luego se presiona CTRL + C
