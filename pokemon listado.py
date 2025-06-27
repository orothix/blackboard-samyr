#pokemon
from codigo_de_pokemon import menu_principal, menu_busqueda
salir = True

lista_pokemon = [
{"ID": "1", "pokemon":"Bulbasaur" ,"tipo":("Planta","Veneno"),"codigo":"A0001"},  
{"ID": "2", "pokemon":"Ivysaur" ,"tipo":("Planta","Veneno"),"codigo":"A0002"},  
{"ID": "3", "pokemon":"Venusaur" ,"tipo":("Planta","Veneno"),"codigo":"A0003"},  
{"ID": "4", "pokemon":"Charmander" ,"tipo":"fuego","codigo":"A0004"},  
{"ID": "5", "pokemon":"Charmeleon" ,"tipo":"fuego","codigo":"A0005"},  
{"ID": "6", "pokemon":"Charizard" ,"tipo":("fuego"," Volador"),"codigo":"A0006"},  
{"ID": "7", "pokemon":"Squirtle" ,"tipo":"Agua","codigo":"A0007"},  
{"ID": "8", "pokemon":"Wartortle" ,"tipo":"Agua","codigo":"A0008"},
{"ID": "9", "pokemon":"Blastoise" ,"tipo":"Agua","codigo":"A0009"},
]

while salir is True:
        
    menu_principal()
    opc = input("Ingrese la opcion: ")
    match opc:
        case "1": #porque se me ocurre hacerlo dificil :(
            registrar_pokemon = input("ingrese el nombre del pokemon para registrar (0 para cancelar el registro): ")
            if registrar_pokemon == 0:
                break
            registrar_id = input("ingrese la id del pokemon: ")
            registrar_tipo = input("ingrese uno o dos tipos del pokemon (separe el tipo con una coma): ").split(",")
            registrar_codigo = input("ingrese el codigo del pokemon: ")
            
            nuevo_pokemon = [
            {"ID": registrar_id, "pokemon":registrar_pokemon,"tipo": registrar_tipo,"codigo":registrar_codigo}    
            ]
            
            lista_pokemon.append(nuevo_pokemon)
                        
        case "2":
            menu_busqueda()
            opc2 = input("\nIngrese la opcion (0 para cancelar): ")
            match opc2:
                case "1":
                    buscar_ID = input("ingrese la ID de la pokedex a buscar: ")
                    for lista_id in lista_pokemon:
                        if lista_id["ID"].lower() == buscar_ID:
                            print("El nombre del pokemon es", lista_id["pokemon"],"Tipo:",lista_id["tipo"],"y su codigo es:",lista_id["codigo"])
                        # else:
                            # print(f"El pokemon con la ID ¨{buscar_ID}¨ no esta en nuestra Pokedex")
                                          
                case "2":
                    buscar_pokemon = input("ingrese el pokemon a buscar: ")
                    for buscar in lista_pokemon:
                        if buscar["pokemon"].lower() == buscar_pokemon.lower():
                            print("El tipo del pokemon es:",buscar["tipo"],"con la ID:",buscar["ID"],"y su codigo es:",buscar["codigo"])
                        # else: 
                            # print(f"el pokemon ¨{buscar_pokemon}¨ no esta en nuestra Pokedex")
              
                # case "3": # aun falta por terminar pero voy bien
                    # buscar_tipo = input("ingrese el tipo del pokemon: ")
                    # for lista_tipo in lista_pokemon:
                        # if lista_tipo["tipo"].lower() == buscar_tipo.lower():
                            # print(lista_tipo["pokemon"], lista_tipo["tipo"],lista_tipo["ID"],lista_tipo["codigo"] )
                        # else:
                            # print(f"no tenemos ningun tipo ¨{buscar_tipo}¨ en nuestra pokedex")
                    
                case "0":
                    print("")
                    
        case "3":
            #ta bug
            remover_pokemon = input("ingrese el pokemon a borrar (0 para cancelar): ")
            if remover_pokemon == 0:
                break
            for remover_pokemon in lista_pokemon:
                lista_pokemon.remove(remover_pokemon)
                break
        case "4":
            print("esto son los pokemon registrados en esta pokedex:")
            print("----------------------------------")
            for listado in lista_pokemon:
                print("ID:", listado["ID"],"Pokemon:", listado["pokemon"],"Tipo:", listado["tipo"])
            print("----------------------------------")
        case "5":
            print("Adios")
            salir = False
        case _:
            print("operacion no valida")