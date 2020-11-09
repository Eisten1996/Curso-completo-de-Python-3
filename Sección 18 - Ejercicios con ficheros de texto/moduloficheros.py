class Fichero(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def leer_fichero(self):
        fichero = open(
            self.nombre, 'rt')
        dato_fichero = fichero.read()
        print(dato_fichero)

    def grabar_fichero(self, texto):
        fichero = open(self.nombre, 'wt')
        fichero.write(texto)
        fichero.close()

    def incluir_fichero(self, texto):
        fichero = open(
            self.nombre, 'at')
        fichero.write(texto)
        fichero.close()
