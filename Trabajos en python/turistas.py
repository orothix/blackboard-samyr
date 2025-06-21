turistas = [
    {"id": "1", "nombre": "John Doe", "pais": "Estados Unidos", "mes": "1"},
    {"id": "2", "nombre": "Emily Smith", "pais": "Estados Unidos", "mes": "3"},
    {"id": "3", "nombre": "Michael Brown", "pais": "Estados Unidos", "mes": "7"},
	{"id": "4", "nombre": "Jessica Davis", "pais": "Estados Unidos", "mes": "11"},
    {"id": "5", "nombre": "Carlos Garcia", "pais": "Mexico", "mes": "5"},
    {"id": "6", "nombre": "Maria Lopez", "pais": "Mexico", "mes": "12"},
    {"id": "7", "nombre": "Joao Silva", "pais": "Brasil", "mes": "6"},
    {"id": "8", "nombre": "Ana Santos", "pais": "Brasil", "mes": "10"},
    {"id": "9", "nombre": "Martin Fernandez", "pais": "Argentina", "mes": "11"},
    {"id": "10", "nombre": "Sofia Gomez", "pais": "Argentina", "mes": "10"},
    {"id": "11", "nombre": "Julian Martinez", "pais": "Argentina","mes": "2"},
    {"id": "12", "nombre": "Agustin Morales", "pais": "Argentina", "mes": "4"},
]

def menu():
    print("\n*****MENU PRINCIPAL*****")
    print("1- Turistas por pais.\n2- Turistas por mes\n3- Eliminar turista\n4- Turistas registrados\n5- Salir")
#---------------------------------------------------------------------------------------------------#
salir = False

while salir is False:
    menu()
    
    opc = input("ingrese operacion: ")    
    match opc:       
        
        case "1":
            pais_ingresado = input("\nIngrese el pais a buscar: ")
            
            for turistas_por_pais in turistas:
                if turistas_por_pais["pais"].lower() == pais_ingresado.lower():
                    print(turistas_por_pais["nombre"])
                else:
                    print(f"no se a encontrado turistas para: {pais_ingresado}")
                    break
#####################################################################################################
        case "2":
            mes_ingresado = input("ingrese el mes del 1 al 12: ")


            cantidad_total = 0
            cantidad_turistas = 0    
                    
            for turista_por_mes in turistas:
                cantidad_total = cantidad_total + 1
                if turista_por_mes["mes"] == mes_ingresado:
                    cantidad_turistas = cantidad_turistas + 1
        
            if cantidad_turistas >= 0:        
                porcentaje = (cantidad_turistas / cantidad_total) * 100
                print(f"el porcentaje de turistas en el mes {mes_ingresado} es de: {porcentaje}%")
            else:
                print(f"no existe un valor para el mes")
#####################################################################################################
        case "3":
            suprimir_ingresado = input("ingrese la ID del turista para eleminar (0 para cancelar): ")
            if suprimir_ingresado == 0:
                break
            for suprimir_ingresado in turistas:
                turistas.remove(suprimir_ingresado)
                break
#####################################################################################################
        case "4":
            print("-------------------------------------------")
            print("ID | NOMBRE | PAIS ")
            for registro in turistas:
                print(registro[ "id"], registro["nombre"], registro["pais"])
        case "5":
            print("progama terminado")
            break
        case _:
            print("operacion no valida (ingrease un numero entero)")
    print("-------------------------------------------")
            