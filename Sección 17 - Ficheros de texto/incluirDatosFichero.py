fichero = open(
    'D:/Desarrollo/Aprendizaje/Curso completo de Python 3/Sección 17 - Ficheros de texto/ficherotext.txt', 'at')

cadena_para_incluir = '\nEsta es la tercera fila del fichero'

fichero.write(cadena_para_incluir)

fichero.close()
