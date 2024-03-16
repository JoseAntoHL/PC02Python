numero = int(input("Escriba el numero: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n - 1)
    
print(f"El factorial de {numero} es: {factorial(numero)}")