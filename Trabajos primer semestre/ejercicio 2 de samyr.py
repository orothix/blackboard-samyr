entradas_disponibles = 50
salir = False
salir_2 = False

def menu_entradas():
    print("******bienvenido a Cine Estrella******")
    print("1- ver entradas disponibles")
    print("2- comprar entradas")
    print("3- salir")

while salir is False:
    menu_entradas()
    opc = input("\ningrese la opcion del 1 al 3: ")

    match opc:
        case "1":
            print("-------------------------")
            print(f"entradas disponibles para la funcion: {entradas_disponibles}")
            print("-------------------------")
        
        case "2":
            if entradas_disponibles == 0:
                print("-------------------------")
                print("entradas agotadas para la funcion")
            
            if entradas_disponibles > 0:
                while salir_2 is False:
                    try:
                        cant_entradas = int(input("ingrese la cantidad de entradas que quiera comprar (0 para cancelar): "))
                    except ValueError:
                        print("ingrese solamente numeros enteros")
                        break
                    if entradas_disponibles >= cant_entradas :
                        if cant_entradas > 0:
                            entradas_disponibles = entradas_disponibles - cant_entradas
                            print("---------------------------")
                            print(f"compra exitosa. quedan {entradas_disponibles} entradas. ")
                            print("---------------------------")
                            break
                        if cant_entradas == 0:
                            break
                        if cant_entradas < 0:
                            print("debes de ingresar un numero superior a 0")
            else:
                print(f"no quedan entradas para esa cantidad (quedan {entradas_disponibles} entradas disponibles)")
        
        case "3":
            salir = True
            print("Gracias por usar el sistema Cine Estrella. ¡hasta la proxima!")
        case _:
            print("-------------------------")
            print("¡¡¡opcion no valida, utilice los numeros del 1-3!!!")