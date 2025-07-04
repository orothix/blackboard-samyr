empleados_antiguos = 0
empleados_ingresados = 0
empleados_no_antiguos = 0
intentos = 0
#---------------------------------------------------------------------------
while not empleados_ingresados > 0: 
    try:
        empleados_ingresados = int(input("ingrese la cantidad de empleados que quiera ingresar: "))
    except ValueError:
        print("Debe de ingresar un numero entero!!!")
    if empleados_ingresados <= 0:
        print("no se puede ingresar numeros negativos, ni cero")
    intentos = intentos + empleados_ingresados 
#---------------------------------------------------------------------------
while intentos > 0:
    print("-----------------------------------------------------------")
    nombre_empleado = input("ingrese el nombre del empleado: ")

    try:
        edad_empleado = int(input(f"ingrese los años de antiguedad de {nombre_empleado}: "))
    except ValueError:
        print("solo se puede ingresar numeros enteros")
        
    if edad_empleado >= 10:
        empleados_antiguos = empleados_antiguos + 1
    elif edad_empleado <= 9:
        empleados_no_antiguos = empleados_no_antiguos + 1
    intentos = intentos - 1
#---------------------------------------------------------------------------
print("-----------------------------------------------------------")
print(f"Se registraron {empleados_antiguos} empleados con mas de 10 años de antiguedad.")        
print(f"Se registraron {empleados_no_antiguos} empleados con 10 o menos años de antiguedad.")        
print("-----------------------------------------------------------")