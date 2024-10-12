
#uso del comando for
foods = ["manzana", "pan", "piña", "cereza", "tomate", "pollo"]

# print(foods[0])
# print(foods[1])
# print(foods[2])
# print(foods[3])
# print(foods[4])

#imprimir todos los elementos uno por uno usando for
for food in foods:
    print(food)

#combinacion de for con if
#pintar sólo si el alimento es pan
for food in foods:
    if food == "pan":
        print(food)
        
#uso de break para parar un bucle for
#en este caso, sólo imprimirá los alimentos hasta que el alimento sea cereza
for food in foods:
    if food == "cereza":
        break
    print(food)
    
#uso de continue:
#se utiliza para que en determinado caso, continue con la ejecucion hacia el siguiente registro
#es decir, se salta ese alimento y pasa al siguiente:
#en este ejemplo, imprime todos excepto la cereza
for food in foods:
    if food == "cereza":
        continue
    print(food)
    
        
#recorrido de un rango
range(1, 8);
for number in range(1, 8):
    print(number)

#recorrido para un arreglo
for cadena in 'hola':
    print(cadena)
        

#comando while:
count = 4
while count <= 10:
    print(count)
    count = count + 1

