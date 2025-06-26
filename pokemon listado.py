#pokemon
from codigo_de_pokemon import menu_principal
salir = True

lista_pokemon = [
{"ID": "1", "pokemon":"Bulbasaur" ,"tipo":"Planta" " Veneno" ,"codigo":"0001"},  
{"ID": "2", "pokemon":"Ivysaur" ,"tipo":"Planta" " Veneno","codigo":"0003"},  
{"ID": "3", "pokemon":"Venusaur" ,"tipo":"Planta" " Veneno","codigo":"0004"},  
{"ID": "4", "pokemon":"Charmander" ,"tipo":"fuego","codigo":"0005"},  
{"ID": "5", "pokemon":"Charmeleon" ,"tipo":"fuego","codigo":"0006"},  
{"ID": "6", "pokemon":"Charizard" ,"tipo":"fuego" " Volador","codigo":"0007"},  
{"ID": "7", "pokemon":"Squirtle" ,"tipo":"Agua","codigo":"0008"},  
{"ID": "8", "pokemon":"Wartortle" ,"tipo":"Agua","codigo":"0009"},
{"ID": "9", "pokemon":"Blastoise" ,"tipo":"Agua","codigo":"0010"},
]

menu_principal()
while salir is True:
        
    opc = input("Ingrese la opcion: ")
    match opc:
        case "1":
            print("hola")
        case "2":
            buscar_pokemon = input("ingrese el pokemon a buscar: ")
            for buscar in lista_pokemon:
                if buscar["pokemon"].lower() == buscar_pokemon.lower():
                    print(f"El tipo del pokemon es: ")
                    print(buscar["tipo"])
                    print("y su codigo es:")
                    print(buscar["codigo"])
                    
            
        case "3":
            print("hola")
        case "4":
            print("hola")
        case "5":
            print("Adios")
            break