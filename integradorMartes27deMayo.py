import os
os.system("cls")

# Programa principal
ListaDePromedios = []

cantidadDeAlumnos = int(input("Cantidad de alumnos: "))
while cantidadDeAlumnos <= 0:
    print("Cantidad de alumnos no valida")
    cantidadDeAlumnos = int(input("Cantidad de alumnos: "))

print("\nIngrese los datos de los alumnos: ")
for i in range(cantidadDeAlumnos):
    id = i + 1

    nombre = input("\nNombre del alumno: ").capitalize()
    apellido = input("Apellido del alumno: ").upper()
    
    codigoDeMateria = int(input("Ingrese el código de la materia\n100: Introducción al pensamiento lógico\n200: Sistemas de computación\n300: Matemática\n400: Inglés\nIngrese aquí:\t"))
    while codigoDeMateria not in [100, 200, 300, 400]:
        print("Dato erroneo. Intente nuevamente")
        codigoDeMateria = int(input("Ingrese el código de la materia\n100: Introducción al pensamiento lógico\n200: Sistemas de computación\n300: Matemática\n400: Inglés\nIngrese aquí:\t"))

    print("\nIngrese las notas del alumno (1 a 10): ")
    sumaNotas = 0
    for i in range(3):
        nota = int(input(f"Nota {i+1}: "))
        while nota < 1 or nota > 10:
            print("Nota no valida")
            nota = int(input(f"Nota {i+1}: "))
        sumaNotas += nota
    promedio = sumaNotas / 3
    ListaDePromedios.append(promedio) 

    tipoDeModalidad = input("\nTipo de modalidad (V/P/M): ").upper()
    while tipoDeModalidad not in ["V", "P", "M"]:
        print("Tipo de modalidad no valida")
        tipoDeModalidad = input("Tipo de modalidad (V/P/M): ").upper()

    # GENERANDO DATOS.

    if codigoDeMateria == 100:
        materia = "Introducción al pensamiento lógico"
    elif codigoDeMateria == 200:
        materia = "Sistemas de computación"
    elif codigoDeMateria == 300:
        materia = "Matemática"
    else: # codigoDeMateria == 400
        materia = "Inglés"
    

    print("\nDATOS DEL ALUMNO:")
    print(f"Nombre: {nombre} {apellido}")
    print(f"Codigo de materia: {codigoDeMateria}")
    print(f"Promedio: {promedio}")
    print(f"Tipo de modalidad: {tipoDeModalidad}")
    print(f"Id: {id}")
    input("\nIngrese cualquier tecla para continuar...")
    os.system("cls")

print("\nLISTA DE PROMEDIOS:")
for i in range(cantidadDeAlumnos):
    print(f"Promedio del alumno {i+1}: {ListaDePromedios[i]}")