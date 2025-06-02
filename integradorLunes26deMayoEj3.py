import os
os.system("cls")

# Programa principal

listaDeNombres = []
listaDeApellidos = []
listaDeAntiguedades = []
listaDeVacaciones = []

cantidadDeEmpleados = int(input("\nIngrese la cantidad de empleados: "))
while cantidadDeEmpleados <= 0:
    print("\nCantidad de empleados no valida")
    cantidadDeEmpleados = int(input("\nIngrese la cantidad de empleados: "))

print(f"\n\nIngrese los datos de los {cantidadDeEmpleados} empleados")
for i in range(cantidadDeEmpleados): 
    # Ingreso el nombre y lo guardo en la lista
    nombre = input(f"\nIngrese el nombre del empleado {i+1}: ").capitalize()
    listaDeNombres.append(nombre)
    
    # Ingreso el apellido y lo guardo en la lista
    apellido = input(f"Ingrese el apellido del empleado {i+1}: ").upper()
    listaDeApellidos.append(apellido)
    
    antiguedad = int(input(f"\nIngrese la antiguedad del empleado {i+1} (entre 0 y 35 años): "))
    while antiguedad < 0 or antiguedad > 35:
        print("\nLa antiguedad debe estar entre 0 y 35 años. Intente nuevamente.")
        antiguedad = int(input(f"\nIngrese la antiguedad del empleado {i+1} (entre 0 y 35 años): "))
    listaDeAntiguedades.append(antiguedad)
    
    if antiguedad>0 and antiguedad<=5:
        vacaciones = 14
    elif antiguedad>5 and antiguedad<=10:
        vacaciones = 21
    elif antiguedad>10 and antiguedad<=20:
        vacaciones = 28
    else:
        vacaciones = 35
    listaDeVacaciones.append(vacaciones)

print("\n\nLos resultados obtenidos son:")
print(f"\nNombre:\tApellido:\tAntiguedad:\tVacaciones:")
for i in range(cantidadDeEmpleados):
    print(f"{listaDeNombres[i]}\t{listaDeApellidos[i]}\t\t{listaDeAntiguedades[i]} años\t\t{listaDeVacaciones[i]} días")

