# Crear un diccionario con los siguientes pares de valores
#   manzana, apple
#   naranja, orange
#   platano, banana
#   limon, lemon
# muestra la traduccion para la palabra 'naranja'
# añade un elemento nuevo como 'piña' y 'pineapple'
# haz un bucle para mostrar todos los elementos del diccionario

frutas = {
    'manzana': 'apple',
    'naranja': 'orange',
    'platano': 'banana',
    'limon': 'lemon'
}

print(frutas['naranja'])

frutas['piña'] = "pineapple"

for fruta, fruits in frutas.items():
    print("{} en ingles es {}".format(fruta, fruits))
