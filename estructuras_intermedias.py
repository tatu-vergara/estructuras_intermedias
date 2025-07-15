matriz = [ [10, 15, 20], [3, 7, 14] ]


cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]


ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}


coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1][0] = 6
print("Matriz modificada:", matriz)

cantantes[0]["nombre"] = "Enrique Martin Morales"
print("Cantantes modificados:", cantantes)

ciudades["México"][2] = "Monterrey"
print("Ciudades modificadas:", ciudades)

coordenadas[0]["latitud"] = 9.9355431
print("Coordenadas modificadas:", coordenadas)

for cantante in cantantes:
    print(f"Nombre - {cantante['nombre']}, País - {cantante['pais']}")

for cantante in cantantes:
    print(cantante["nombre"])
for cantante in cantantes:
    print(cantante["pais"])

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

for clave, lista in costa_rica.items():
    print(len(lista), clave.upper())
    for elemento in lista:
        print(elemento)

print(len(costa_rica))