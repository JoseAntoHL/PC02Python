numero = input("Ingrese el numero: ")
digito = input("ingrese el digito: ")

def funcion(numero, digito):
    contador = 0
    for dig in numero:
        if dig == digito:
            contador += 1
    return contador

print(f"Cantidad de veces {digito} en el número es: {funcion(numero, digito)}")