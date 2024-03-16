def quitar_vocales(texto):
    vocales = 'aeiouAEIOU'
    sin_vocales = ''

    for char in texto:
        if char not in vocales:
            sin_vocales += char
    return sin_vocales

texto = input("Ingrese un texto: ")
resultado = quitar_vocales(texto)

print(f"Texto sin vocales: {resultado}")