cantidad = int(input("Cuantas veces:"))

def fibonacci(n):
    a = 0
    b = 1
    fibonaccis = [a,b]

    if n <= 0:
        return []
    if n == 1:
        return [a]
    if n == 2:
        return fibonaccis
    for i in range(2,n):
        c = a + b
        fibonaccis.append(c)
        a = b
        b = c

    return fibonaccis

resultado = fibonacci(cantidad)

print(resultado)