# Crear una clase 'Coche' que tenga estos atributos:
# marca, color, combustible y cilindrina

# Crear la funcion '__init__' que asigna los parametros de la clase a los atributos de la clase

# Crear otraa funcion 'mostrar_caracteristicas' que mediante print muestre por pantalla
# las caracteristicas (o atributos)  que tiene el coche

# Crear un objeto 'coche1' de la clase 'Coche' con los atributos 'Ope1', 'rojo', 'gasolina', '1.6'

# Ejecutar la funcion 'mostrar_caracteristicas' del objecto 'coche1'

class Coche:
    def __init__(self, marca, color, combustible, cilindrina):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrina = cilindrina

    def mostrar_caracteristicas(self):
        print("marca : "+self.marca)
        print("color : "+self.color)
        print("combustible : "+self.combustible)
        print("cilindrina : "+self.cilindrina)


coche1 = Coche('Ope1', 'rojo', 'gasolina', '1.6')

coche1.mostrar_caracteristicas()
