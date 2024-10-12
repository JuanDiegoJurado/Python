#definicion de una function
def hello():
    print("hello world")

#llamada de una function
hello()

#definicion de function con parametros
def hello(name):
    print("hello: " + name)
    
hello("Juan Diego!")

#definicion de function con parametros con valores por defecto
def hello(name = "person"):
    print("hello: " + name)
    
hello()


#funcion suma
def suma(parametro1, parametro2):
    return parametro1 + parametro2
    
#llamada de la funcion
suma(5, 10)
print(suma(5, 10))

#funciones lambda:
add = lambda numero1, numero2: numero1 + numero2
print(add(10, 30))
    