# pickle - modulo para grabar ficheros bonarios

import pickle

fichero = open("fichero colores.pckl", "rb")

lista_leida_fichero = pickle.load(fichero)

print(lista_leida_fichero)
