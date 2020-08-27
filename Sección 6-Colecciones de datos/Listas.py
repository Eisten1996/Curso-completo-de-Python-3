# Lista
colores = ["rojo", "amarillo", "verde"]
print(colores)

print(colores[0])
print(colores[1])

colores[1] = "azul"
print(colores)

print(len(colores))

colores.append("naranja")
print(colores)
print(colores[3])

colores.remove("rojo")
print(colores)

for color in colores:
    print(color)

colores.clear()
print(colores)
