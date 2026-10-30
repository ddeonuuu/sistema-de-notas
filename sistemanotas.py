nombre = []
notas = []
promedio = []
aprobado = []
reprobado = []
opcion = "S"

while opcion == "S":
    print("============= MENU DE OPCIONES =============")
    print("1.[A]gregar")
    print("2.[M]odificar")
    print("3.[E]liminar")
    print("4.[V]isualizar")
    print("5.[B]uscar")
    print("6.[S]alir")
    opcion = input("Seleccione una opción: ").upper() 
    if opcion == "A":
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        while nombre_alumno == "":
            print("El nombre del alumno no puede estar vacío.") 
            nombre_alumno = input("Ingrese el nombre del alumno: ")
        if nombre_alumno != "":
            nombre.append(nombre_alumno)
            print(f"Alumno {nombre_alumno} agregado correctamente.")
            cantidad_notas = int(input("Ingrese la cantidad de notas: "))
            if cantidad_notas <= 0:
                print("La cantidad de notas debe ser mayor a cero.")
            else:
                notas_alumno = []
                for i in range(cantidad_notas):
                    nota = float(input(f"Ingrese la nota {i + 1}: "))
                    while nota < 2 or nota > 7:
                        print("La nota debe estar entre 2 y 7.")
                        nota = float(input(f"Ingrese la nota {i + 1}: "))
                    notas_alumno.append(nota)
                notas.append(notas_alumno)
                promedio_alumno = sum(notas_alumno) / cantidad_notas
                promedio.append(promedio_alumno)
                if promedio_alumno >= 4:
                    aprobado.append(nombre_alumno)
                else:
                    reprobado.append(nombre_alumno)
    if opcion == "M":
        nombre_alumno = input("Ingrese el nombre del alumno a modificar: ")
        if nombre_alumno in nombre:
            posicion = nombre.index(nombre_alumno)
            nuevo = input("Ingrese el nuevo nombre: ")
            nombre[posicion] = nuevo
            print(f"Nombre del alumno modificado a {nuevo}.")
        else:
            print("Estudiante no encontrado.")
    if opcion == "E":
        nombre_alumno = input("Ingrese el nombre del alumno a eliminar: ")

        if nombre_alumno in nombre:
            nombre.remove(nombre_alumno)
            print(f"Alumno {nombre_alumno} eliminado correctamente.")
        else:
            print("Estudiante no encontrado.")
    if opcion == "V":
        print("============= LISTA DE ALUMNOS =============")
        print(nombre)
    if opcion == "B":
        nombre_alumno = input("Ingrese el nombre del alumno a buscar: ")
        if nombre_alumno in nombre:
            print(f"Alumno {nombre_alumno} encontrado.")
        else:
            print("Estudiante no encontrado.")                      