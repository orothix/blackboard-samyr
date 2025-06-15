#base de la caluladora
def menu():
    print("------Calculadora-----")

    print("1- sumar")
    print("2- restar")
    print("3- multiplicar")
    print("4- dividir")
    print("5- salir")

def ingrese_numero():
    n1 = float(input("ingrese el primer numero: "))
    n2 = float(input("ingrese el segundo numero: "))
    print("-------------")
    if opc == 1:
        print(f"el resultado es: {n1+n2}")
    if opc == 2:
        print(f"el resultado es: {n1-n2}")
    if opc == 3:
        print(f"el resultado es: {n1*n2}")
    if opc == 4:
        while n2 == 0:
            print("el dividor no puede ser 0")
            n2 = float(input("vuelva a ingresar el divisor: "))
        print(f"el resultado es: {n1/n2}")
    print("")

#calculadora
salir = False
while True:

    menu()
    
    opc = int(input("ingrese la operacion: "))

    if opc == 1:
        ingrese_numero()
    elif opc == 2:
        ingrese_numero()
    elif opc == 3:
        ingrese_numero()
    elif opc == 4:
        ingrese_numero()
    elif opc == 5:
        break
    else:
        print("----------------------")
        print("!!!operacion no valida")
print("hasta luego :)")