import moduloficheros

fichero = moduloficheros.Fichero('fichero2.txt')

fichero.grabar_fichero(
    'Hola, esta es la linea que vamos a grabar en el fichero de texto')

fichero.incluir_fichero('\ntexto extra')

fichero.leer_fichero()
