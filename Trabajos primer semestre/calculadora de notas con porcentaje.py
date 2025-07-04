
nota_total = 0
salir = True
#-----------------
while salir is True:
    notas_ingresadas = float(input("ingrese la nota (ingrese 0 para terminar): "))
    if notas_ingresadas == 0:
        break
    porcentaje_ingesado = float(input("ingrese el porcentaje de la nota: "))

 

    nota_total = notas_ingresadas * porcentaje_ingesado

nota_total = nota_total / 100
print(f"la nota es: {nota_total}")