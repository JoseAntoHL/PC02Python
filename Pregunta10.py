meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

fecha = input("Ingrese una fecha (en formato Mes dia, año): ")

def convertir_fecha(fecha):
    partes = fecha.split()
    if len(partes) < 3:
        return "Formato de fecha no válido"

    dia = partes[-2].strip(',')
    mes = partes[0] if partes[0] in meses else partes[0].capitalize()
    anio = partes[-1]

    mes_numero = str(meses.index(mes) + 1).zfill(2)

    return f"{anio}-{mes_numero}-{dia.zfill(2)}"

fechaf = convertir_fecha(fecha)
print(f"Fecha formateada: {fechaf}")


