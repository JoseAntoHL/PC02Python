numero = int(input("Escriba el numero: "))

def esprimo(n):
    if numero <= 1:
        return "no primo"
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return "no primo"
    return "primo"
    
print(f"El numero {numero} es {esprimo(numero)}")