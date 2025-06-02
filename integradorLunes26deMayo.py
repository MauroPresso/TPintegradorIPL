import os
os.system("cls")

# Programa principal.
listaDePromedios = []
listaDeApellidos = []
listaDeCondicion = []
cantidadDeEstudiantes = 2
cantidadDeNotas = 3
print(f"\n\nIngrese los datos de los {cantidadDeEstudiantes} estudiantes: ")
for i in range(cantidadDeEstudiantes):
    print(f"\n\nEstudiante ingrese los datos del estudiante {i+1}: ")
    
    # Ingreso el apellido y lo guardo en la lista.
    apellido = input(f"\nIngrese el apellido del estudiante {i+1}: ").upper()
    listaDeApellidos.append(apellido)
    
    # Calculo el promedio de las notas y lo guardo en la lista.
    print(f"\nIngrese las {cantidadDeNotas} notas del estudiante {i+1}: ")
    sumaNotas = 0
    for j in range(cantidadDeNotas):
        nota = int(input(f"\nIngrese la nota {j+1} (entre 1 y 10) del estudiante {i+1}: "))
        while nota<=0 or nota>10: 
            print("\nNota incorrecta, ingrese una nota entre 1 y 10: ")
            nota = int(input(f"\nIngrese la nota {j+1} (entre 1 y 10) del estudiante {i+1}: "))
        sumaNotas = sumaNotas + nota
    promedio = sumaNotas/cantidadDeNotas
    listaDePromedios.append(promedio)
    
    if promedio>=8:
        condicion = "Promoción"
    elif promedio>=6:
        condicion = "Regular"
    elif promedio>=4:
        condicion = "Libre"
    else:
        condicion = "Insuficiente"
    listaDeCondicion.append(condicion)

# Muestro los resultados.
print(f"\n\nLos resultados del cursado son: ")
for i in range(cantidadDeEstudiantes):
    print(f"\nEl estudiante {i+1} con apellido {listaDeApellidos[i]} tiene un promedio de {listaDePromedios[i]} y su condición es de {listaDeCondicion[i]}")
    
