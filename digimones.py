digimones = [
    {
        "id": 1,
        "name": "Agumon",
        "png": "https://digi-api.com/images/digimon/w/Agumon.png",
        "level": "Child"
    },
    {
        "id": 2,
        "name": "Airdramon",
        "png": "https://digi-api.com/images/digimon/w/Airdramon.png",
        "level": "Adult"
    },
    {
        "id": 3,
        "name": "Angemon",
        "png": "https://digi-api.com/images/digimon/w/Angemon.png",
        "level": "Adult"
    },
    {
        "id": 4,
        "name": "Betamon",
        "png": "https://digi-api.com/images/digimon/w/Betamon.png",
        "level": "Child"
    }
]

print("--------------------")
for digimon in digimones:
    print("id:" ,digimon["id"])
    print(digimon["name"])
    print(digimon["level"])
    print(digimon["png"])
    print("--------------------")
    