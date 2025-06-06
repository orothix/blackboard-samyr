personas = [
    {
        "nivel": 1,
        "arcano": "El Loco",
        "nombre": "Izanagi"
    },
    {
        "nivel": 2,
        "arcano": "El Mago",
        "nombre": "Pixie"
    },
    {
        "nivel": 2,
        "arcano": "El Carro",
        "nombre": "Slime"
    },
    {
        "nivel": 3,
        "arcano": "El Diablo",
        "nombre": "Ukobach" 
    },                
    {
        "nivel": 4,
        "arcano": "El Mago",
        "nombre": "Jiraiya" 
    },
    {
        "nivel": 4,
        "arcano": "El Carro",
        "nombre": "Tomoe" 
    },
]
#---------------------------------------------------------

print("------------------")
for persona in personas:
    print("nivel:", persona["nivel"])
    print("arcano:", persona["arcano"])
    print("nombre:", persona["nombre"])
    print("------------------")