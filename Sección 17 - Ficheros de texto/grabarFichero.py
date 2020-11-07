# Grabar un fichero de texto

fichero = open('fichero_para _grabar.txt', 'wt')

cadena_texto = 'Hola, esta es la linea que vamos a grabar en el fichero de texto'

fichero.write(cadena_texto)

fichero.close()
