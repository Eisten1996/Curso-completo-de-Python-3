# Crear el diccionario "frutas"
# frutas = {"manzanas":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}
#
# Grabar esta estructura de datos "frutas" en un fichero binario "fichero.pckl"
# Ya que en un fichero de texto, solo se guarda caracteres, pero no se puede guardar estructuras
#
# Recuperar esta estructura de datos del fichero "fichero.pckl"
# Verificar que sigue siendo un diccionario, ejecutando el metodo .values()

import pickle

frutas = {"manzanas": "apple", "naranja": "orange",
                 "platano": "banana", "limon": "lemon"}

fichero = open("fichero frutas.pckl", "wb")

pickle.dump(frutas, fichero)

fichero.close()

fichero = open("fichero frutas.pckl", "rb")

lista_leida_fichero = pickle.load(fichero)

print(frutas.values())
print(lista_leida_fichero.values())
