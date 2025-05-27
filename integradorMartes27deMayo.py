import os
os.system("cls")

# Programa principal
sumaNotas = 0
ListaDePromedios = []

cantidadDeAlumnos = int(input("Cantidad de alumnos: "))
while cantidadDeAlumnos <= 0:
    print("Cantidad de alumnos no valida")
    cantidadDeAlumnos = int(input("Cantidad de alumnos: "))

print("\nIngrese los datos de los alumnos: ")
for i in range(cantidadDeAlumnos):

    id = i + 1

    nombre = input("Nombre del alumno: ").capitalize()
    apellido = input("Apellido del alumno: ").upper()
    
    codigoDeMateria = (i+1)*100

    print("Ingrese las notas del alumno (1 a 10): ")
    for i in range(3):
        nota = int(input(f"Nota {i+1}: "))
        while nota < 1 or nota > 10:
            print("Nota no valida")
            nota = int(input(f"Nota {i+1}: "))
        sumaNotas += nota
    promedio = sumaNotas / 3
    ListaDePromedios.append(promedio) 

    tipoDeModalidad = input("Tipo de modalidad (V/P/M): ").upper()
    while tipoDeModalidad not in ["V", "P", "M"]:
        print("Tipo de modalidad no valida")
        tipoDeModalidad = input("Tipo de modalidad (V/P/M): ").upper()

    print("\nDATOS DEL ALUMNO:")
    print(f"Nombre: {nombre} {apellido}")
    print(f"Codigo de materia: {codigoDeMateria}")
    print(f"Promedio: {promedio}")
    print(f"Tipo de modalidad: {tipoDeModalidad}")
    print(f"Id: {id}")
    input("\nIngrese cualquier tecla para continuar...")

print("\nLISTA DE PROMEDIOS:")
for i in range(cantidadDeAlumnos):
    print(f"Promedio del alumno {i+1}: {ListaDePromedios[i]}")