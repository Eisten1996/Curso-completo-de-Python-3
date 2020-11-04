# Clases y objetos. Programacion orientada a objetos. POO

class ClaseSilla:
    color = 'blanco'
    precio = 100


objetoSilla1 = ClaseSilla()

print(objetoSilla1.color)
print(objetoSilla1.precio)

objetoSilla2 = ClaseSilla()

objetoSilla2.color = 'verde'
objetoSilla2.precio = 120

print(objetoSilla2.color)
print(objetoSilla2.precio)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print('Hola me llamo {} y tengo {} años'.format(self.nombre, self.edad))


persona1 = Persona('Juan', 37)

print(persona1.nombre)
print(persona1.edad)

persona1.saludar()
