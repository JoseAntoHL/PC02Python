lista = []
listapares = []
listaimpares = []

respuesta = str(input("Desea ingresar un número?(SI/NO)"))
respuestaup = respuesta.upper()

while respuestaup == "SI":
    numero = int(input("Ingrese el numero: "))
    lista.append(numero)

    respuesta = str(input("Desea ingresar un número?(SI/NO)"))
    respuestaup = respuesta.upper()
    if(respuestaup == "SI"):    
        continue
    else:
        print(f"Numeros ingresados:  {lista}")
        break

for i in lista:
    if (i % 2 == 0):
        listapares.append(i)
    else:
        listaimpares.append(i)

cpares = len(listapares)
cimpares = len(listaimpares)
print(f"Cantidad de números pares: {cpares}")
print(f"Cantidad de números impares: {cimpares}")