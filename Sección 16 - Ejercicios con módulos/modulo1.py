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


media = lambda nota1, nota2, nota3: (nota1+nota2+nota3)/3


