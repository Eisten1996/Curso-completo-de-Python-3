# pickle - modulo para grabar ficheros bonarios

import pickle

lista_colores = ["azul", "verde", "rojo", "amarillo"]

fichero = open("fichero colores.pckl", "wb")

pickle.dump(lista_colores, fichero)

fichero.close()
