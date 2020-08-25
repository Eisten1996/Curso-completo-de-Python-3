diccionario_colores = {
    "red": "rojo",
    "blue": "azul",
    "yellow": "amarillo"
}
print(diccionario_colores)

print(diccionario_colores["red"])

valor = diccionario_colores["blue"]
print(valor)

diccionario_colores["black"] = "negro"
print(diccionario_colores)

print(diccionario_colores.pop("yellow"))
print(diccionario_colores)

del(diccionario_colores["black"])
print(diccionario_colores)

for color in diccionario_colores:
    print(color)

for clave, valor in diccionario_colores.items():
    print(clave, valor)
