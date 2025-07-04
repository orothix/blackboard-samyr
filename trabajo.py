peliculas = []

cantidad = int(input("ingrese la cantidad de peliculas a guardar: "))

for i in range(1, cantidad+1):
    print("------------------------------")  
    nombre = input("ingrese el nombre de la pelicula: ")
    anio = int(input("ingrese el año de estreno: "))

    peliculas.append({
        "nombre": nombre,
        "año": anio
    })
    
print("----------peliculas----------")
# for indice, peliculas in enumerate(peliculas):
#     print("nombre:",nombre,"año:",anio)

# for pelicula in peliculas:
#     print("Nombre:", pelicula["nombre"], "Año:", pelicula["año"])

for peliculas in peliculas:
    print("nombre:",nombre,"año:",anio)
