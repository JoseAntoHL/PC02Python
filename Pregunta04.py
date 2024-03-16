alumnos = []

cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for i in range(cant_alumnos):
    nombre = input("Alumno: ")
    notas_alumno = []
    
    for y in range(3):
        nota = int(input(f"Ingrese la nota {y + 1}: "))
        notas_alumno.append(nota)
            
    alumno = {"Alumno": nombre, "Notas" : notas_alumno}

    alumnos.append(alumno)

print("Lista de alumnos")
for alumno in alumnos:
    print(f"Alumno: {alumno ['Alumno']}, Notas: {alumno ['Notas']}")


