#Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5, 
#en el rango de 1500 y 2700 (ambos incluidos).


for anio in range(1499,2701):
    if (anio % 7 == 0 and anio % 5 == 0):
        print(anio)
