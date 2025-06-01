import os
os.system("cls")

# Programa principal
ListaDePromedios = []

#Cantidad de promocionados, regulares, libres y ausentes
contPromo,contRegu,contLibres,contAus = 0,0,0,0

#Cantidad de estudiantes por materia
contIPL,contSist,contMath,contEngl = 0,0,0,0

#Cantidad de promocionados por materia
contPromoIPL,contPromoSist,contPromoMath,contPromoEngl = 0,0,0,0

#Cantidad de regulares por materia
contReguIPL,contReguSist,contReguMath,contReguEngl = 0,0,0,0

#Cantidad de alumnos libres por materia
contLibresIPL,contLibresSist,contLibresMath,contLibresEngl = 0,0,0,0

#Cantidad de ausentes por materia
contAusIPL,contAusSist,contAusMath,contAusEngl = 0,0,0,0

#Cantidad de estudiantes según modalidad y materia
contIPLPresencial,contIPLVirtual,contIPLMixta = 0,0,0
contSistPresencial,contSistVirtual,contSistMixta = 0,0,0
contMathPresencial,contMathVirtual,contMathMixta = 0,0,0
contEnglPresencial,contEnglVirtual,contEnglMixta = 0,0,0
#...
cantidadDeAlumnos = int(input("Cantidad de alumnos: "))
while cantidadDeAlumnos <= 0:
    print("Cantidad de alumnos no valida")
    cantidadDeAlumnos = int(input("Cantidad de alumnos: "))

print("\n\nIngrese los datos de los alumnos: ")
for i in range(cantidadDeAlumnos):
    id = i + 1

    nombre = input("\n\nNombre del alumno: ").capitalize()
    apellido = input("Apellido del alumno: ").upper()
    
    codigoDeMateria = int(input("\nIngrese el código de la materia\n100: Introducción al pensamiento lógico\n200: Sistemas de computación\n300: Matemática\n400: Inglés\nIngrese aquí: "))
    while codigoDeMateria not in [100, 200, 300, 400]:
        print("Dato erroneo. Intente nuevamente")
        codigoDeMateria = int(input("\nIngrese el código de la materia\n100: Introducción al pensamiento lógico\n200: Sistemas de computación\n300: Matemática\n400: Inglés\nIngrese aquí: "))

    print("\nIngrese las notas del alumno (1 a 10): ")
    sumaNotas = 0
    for i in range(3): # Son 3 notas.
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

    # Definiendo la materia.
    if codigoDeMateria == 100:
        materia = "Introducción al pensamiento lógico"
        profesor = "Juan Perez"
    elif codigoDeMateria == 200:
        materia = "Sistemas de computación"
        profesor = "Andrea Garrido"
    elif codigoDeMateria == 300:
        materia = "Matemática"
        profesor = "Sebastián Prost"
    else: # codigoDeMateria == 400
        materia = "Inglés"
        profesor = "Andrea Gomez"

    # Definiendo la condición del alumno.
    if promedio>=7:
        condicion = "Promoción"
        defensa = "NO"
        examen = "NO"
        fecha = "Directo"
    elif promedio>=4:
        condicion = "Regular"
        defensa = "SI"
        examen = "SI"
        fecha = "10/07/2025"
    elif promedio>=3:
        condicion = "Libre"
        defensa = "NO"
        examen = "SI"
        fecha = "14/07/2025"
    else:
        condicion = "Ausente"
        defensa = "NO"
        examen = "NO"
        fecha = "Recursa"
    
    # Definiendo el tipo de modalidad.
    if tipoDeModalidad == "V":
        modalidad = "Virtual"
    elif tipoDeModalidad == "P":
        modalidad = "Presencial"
    else:
        modalidad = "Mixta"

    # Definiendo aula y horario.
    if modalidad == "Presencial":
        if materia == "Introducción al pensamiento lógico":
            aula = "1"
            horario = "Lunes 19:00 a 21:00"
        elif materia == "Sistemas de computación":
            aula = "8"
            horario = "Jueves 20:30 a 22:00"
        elif materia == "Matemática":
            aula = "12"
            horario = "Viernes 19:00 a 21:00"
        else: # materia == "Inglés"
            aula = "15"
            horario = "Martes 19:00 a 20:30"
    elif modalidad == "Virtual":
        if materia == "Introducción al pensamiento lógico":
            aula = "Zoom"
            horario = "Lunes 19:00 a 21:00"
        elif materia == "Sistemas de computación":
            aula = "Meet"
            horario = "Jueves 20:30 a 22:00"
        elif materia == "Matemática":
            aula = "Meet"
            horario = "Viernes 19:00 a 21:00"
        else: # materia == "Inglés"
            aula = "Zoom"
            horario = "Martes 19:00 a 20:30"
    else: # modalidad == "Mixta"
        if materia == "Introducción al pensamiento lógico":
            aula = "Zoom"
            horario = "Miércoles 19:00 a 20:40"
        elif materia == "Sistemas de computación":
            aula = "8"
            horario = "Lunes 19:00 a 21:00"
        elif materia == "Matemática":
            aula = "12"
            horario = "Miércoles 21:00 a 22:40"
        else: # materia == "Inglés"
            aula = "Zoom"
            horario = "Jueves 19:00 a 20:30"
        

    print("\nDATOS DEL ALUMNO:")
    print(f"Nombre: {nombre} {apellido}")
    print(f"Id: {id}")
    print(f"Modalidad: {modalidad}")
    print(f"Materia: {materia}")
    print(f"Profesor: {profesor}")
    print(f"Aula: {aula}")
    print(f"Horario: {horario}")
    print(f"Promedio: {promedio}")
    print(f"Condicion: {condicion}")
    print(f"Defensa: {defensa}")
    print(f"Examen: {examen}")
    print(f"Fecha: {fecha}")
    input("\nIngrese cualquier tecla para continuar...")
    os.system("cls")

print("\nREPORTE FINAL:")

# Inciso b)
print(f"\n\n\nTotal de alumnos por materia:")
print(f"\nIntroducción al pensamiento lógico: {contIPL}")
print(f"Sistemas de computación: {contSist}")
print(f"Matemática: {contMath}")
print(f"Inglés: {contEngl}")

# Inciso g)
print(f"\n\n\nTotal de alumnos por modalidad y materia:")
print("\nIntroducción al pensamiento lógico:")
print(f"Presencial: {contIPLPresencial}")
print(f"Virtual: {contIPLVirtual}")
print(f"Mixta: {contIPLMixta}")
print("\n\nSistemas de computación:")
print(f"\nPresencial: {contSistPresencial}")
print(f"Virtual: {contSistVirtual}")
print(f"Mixta: {contSistMixta}")
print("\n\nMatemática:")
print(f"\nPresencial: {contMathPresencial}")
print(f"Virtual: {contMathVirtual}")
print(f"Mixta: {contMathMixta}")
print("\n\nInglés:")
print(f"\nPresencial: {contEnglPresencial}")
print(f"Virtual: {contEnglVirtual}")
print(f"Mixta: {contEnglMixta}")

# Inciso a)
print(f"\n\n\nTotal de alumnos por condición:")
print(f"\nTotal de alumnos promocionados: {contPromo}")
print(f"Total de alumnos regulares: {contRegu}")
print(f"Total de alumnos libres: {contLibres}")
print(f"Total de alumnos ausentes: {contAus}")

# Inciso c)
print(f"\n\n\nTotal de alumnos promocionados por materia:")
print(f"\nIntroducción al pensamiento lógico: {contPromoIPL}")
print(f"Sistemas de computación: {contPromoSist}")
print(f"Matemática: {contPromoMath}")
print(f"Inglés: {contPromoEngl}")

# Inciso d)
print(f"\n\n\nTotal de alumnos regulares por materia:")
print(f"\nIntroducción al pensamiento lógico: {contReguIPL}")
print(f"Sistemas de computación: {contReguSist}")
print(f"Matemática: {contReguMath}")
print(f"Inglés: {contReguEngl}")

# Inciso e)
print(f"\n\n\nTotal de alumnos libres por materia:")
print(f"\nIntroducción al pensamiento lógico: {contLibresIPL}")
print(f"Sistemas de computación: {contLibresSist}")
print(f"Matemática: {contLibresMath}")
print(f"Inglés: {contLibresEngl}")

# Inciso f)
print(f"\n\n\nTotal de alumnos ausentes por materia:")
print(f"\nIntroducción al pensamiento lógico: {contAusIPL}")
print(f"Sistemas de computación: {contAusSist}")
print(f"Matemática: {contAusMath}")
print(f"Inglés: {contAusEngl}")

print("\n\n\nLISTA DE PROMEDIOS:")
for i in range(cantidadDeAlumnos):
    print(f"Promedio del alumno {i+1}: {ListaDePromedios[i]}")